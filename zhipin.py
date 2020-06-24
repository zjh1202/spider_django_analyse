# @Time : 2020/6/18 10:05
# @Author : JunHong
# @File : zhipin.py

# !/usr/bin/python3
# encoding: utf-8

import requests
from lxml import etree
import pymysql
import time

def spider(keyword, page):
    headers = {
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
            'cookie':'__zp__pub__=; Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c=1590134891; lastCity=101280100; _bl_uid=hCkbvb9X439r55mtCm8ydUyc5kas; __c=1592447827; __g=-; __l=l=%2Fwww.zhipin.com%2Fguangzhou%2F&r=&friend_source=0&friend_source=0; __zp__pub__=; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1592374156,1592443674,1592447827,1592463693; t=uPytV2oMFhUqji0h; wt=uPytV2oMFhUqji0h; __a=43818746.1590134882.1592443674.1592447827.448.27.36.257; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1592464111; __zp_stoken__=1832afEojVRRPDnh4azRRP2RvPBEGNkoFJy9STj8yNEoWalIEAGVoe2MKen48XXd%2BJjswZGEwX3R%2FIFwYLjd7GEV7MjsONSV4aXpldQFTPTwSXAMdf14CXDxSAx4ANRg1ZAJ1GxxEXQNpOiw%3D'
        }
    url = 'https://www.zhipin.com/c101280100/?query={}&page={}&ka=page-1'.format(keyword, page)
    response = requests.get(url, headers=headers)
    html_str = response.text
    # 建立数据库连接
    connection = pymysql.connect(host='localhost', port=3309, user='root', password='', db='spider',
                                 charset='utf8')
    # 创建操作游标
    cursor = connection.cursor()

    html = etree.HTML(html_str)
    # 工作列表
    job_list = html.xpath("//*[@id='main']/div/div[2]/ul/li")

    for i in range(len(job_list)):
        # 工作名称
        job = html.xpath("//div[@id='main']/div/div[2]/ul/li[{}]/div/div[1]/div[1]/div/div[1]/span[1]/a/text()".format(i+1))[0]
        # 工作公司
        company = html.xpath('//div[@id="main"]/div/div[2]/ul/li[{}]/div/div[1]/div[2]/div/h3/a/text()'.format(i+1))[0]
        # 工资
        wages = html.xpath('//div[@id="main"]/div/div[2]/ul/li[{}]/div/div[1]/div[1]/div/div[2]/span/text()'.format(i+1))[0]
        # 技术需求
        technologys = html.xpath('//div[@id="main"]/div/div[2]/ul/li[{}]/div/div[2]/div[1]/span/text()'.format(i+1))
        technology = ";".join(technologys)
        # 公司类型
        coustompage = html.xpath('//div[@id="main"]/div/div[2]/ul/li[{}]/div/div[1]/div[2]/div/p/a/text()'.format(i + 1))[0]
        # 工作地址
        url = html.xpath('//*[@id="main"]/div/div[2]/ul/li[{}]/div/div[1]/div[1]/div/div[1]/span[1]/a/@href'.format(i+1))[0]
        content = {
            'job': job,
            'company': company,
            'wages': wages,
            'technology': technology,
            'coustompage': coustompage,
            'url': "zhipin.com" + url
        }
        sql = "insert into zhipin" \
              "(job,company,wages,technology,coustompage,url,keyword)" \
              "value" \
              "('%s','%s','%s','%s','%s','%s','%s')" % (content['job'], content['company'], content['wages'],
                                                             content['technology'], content['coustompage'],
                                                             content['url'], keyword)
        # 执行sql语句
        cursor.execute(sql)
        # 保存修改
        connection.commit()
        print('添加数据成功')

    # 关闭操作游标
    cursor.close()
    # 关闭数据库连接
    connection.close()
    print('关闭链接数据库')



if __name__ == "__main__":
    keyword = "算法"
    for page in range(1, 11):
        spider(keyword, page)
        time.sleep(60)
