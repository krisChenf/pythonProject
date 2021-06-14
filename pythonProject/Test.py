# coding=utf-8

import json,requests
"""
input等待用户输入 挂起线程等待用户输入
特殊的注释来声明编码格式，
只有入口模块的 __name__ 变量,会被赋值为main.
def f1(a, b, c=0, *args, **kw):  可变参数 关键字参数 组合参数
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
    *args是可变参数，args接收的是一个tuple；
**kw是关键字参数，kw接收的是一个dict。
from
response
@property 注解
"""

if __name__ == 'Test':
 print('PyCharm00')
print(__name__)
def searchPackages():
    packageNum = input('请输入运单号码：')
    ua = 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko'
    header = {"User-Agent": ua}
    url1 = 'https://www.kuaidi100.com/autonumber/autoComNum?resultv2=1&text=' + packageNum
    print("----------------------------------------")
    print(requests.get(url1,headers=header))
    print(type(requests.get(url1,headers=header)))
    print("-------------------------00---------------")
    print(type(json.loads(requests.get(url1,headers=header).text)))
    # dict json lodas 返回类型 String text @property 是dic 类型通过 dict 取出键值对即可
    companyName = json.loads(requests.get(url1,headers=header).text)['auto'][0]['comCode']
    print(companyName)
    url2 = 'https://www.kuaidi100.com/query?type=' + companyName + '&postid=' + packageNum
    print("时间 |地点|跟踪进度\n")
    print(json.loads(requests.get(url2, headers=header).text))
    responese = json.loads(requests.get(url2, headers=header).text)['data']
    for item in responese:
        print('---------------')
        print(item['time'],item['context'])
searchPackages()
# 75466794698816 {"comCode":"","num":"75466794698816","auto":[{"comCode":"zhongtong","lengthPre":14,"name":"中通快递"}],"autoDest":[]}