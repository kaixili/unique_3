#!/usr/bin/env python
# coding=utf-8
'''调用函数inpuy.key() 在括号里输入需要搜索的字符串

   字符串需要带引号(')(")'''

import urllib.parse
from output import *

#if __name__ == '__main__':
    #keyword = input("请输入关键词-->")

def key(keyword):
    print('======请稍等=========================================\n------等待请求返回,等待时间时间取决于服务器响应------')
    
    keyword_quote = urllib.parse.quote(keyword)
    target = "http://ftp.lib.hust.edu.cn/search*chx/X?SEARCH="
    tail = "&SORT=D&image.x=0&image.y=0"

    url = target + keyword_quote + tail

    result_list(url)
    nextpage(url)

    print('======结束==========')