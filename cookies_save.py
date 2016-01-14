#coding:utf-8
import cookielib
import urllib2
import urllib
import json
import excel
import proplanbaen
import time

# 验证码登陆
def getlogindata():
    postdata = urllib.urlencode({
            'mobile':'15583581921',
            'validateCode':'3965'
        })
    return postdata


# 计划书费率参数
def getpama():
    postdata = urllib.urlencode({
            'insuranceTypeId':'168', #险种id
            'sex':'1',                 #性别
            'age':"42",               #年龄
            'years':"10",             #缴费期间
            'baoe':"10",              #保额
            'baofei':"4113",          #保费
            'idea':"-1",              #保险理念
            'cname':"",
            'csex':"1"
        })
    return postdata


#平安 尊享人生
def getp(msex,mage,myears):
    data = urllib.urlencode({'jsonParameters':'{"baotype":1155,"insuranceTypeId":193,"hasSocial":true,"sex":'+str(msex)+',"age":'+str(mage)+',"isApply":false,"applySex":1,"applyAge":18,"idea":-1,"csex":1,"additionalShow":{"zhuyuanRJT":true,"zhuyuanYl":true,"yiwaiYl":true,"yiwaiSh_2":true},"years":'+str(myears)+',"baoe1155":10000,"callMethod":1}',
                             "baotype":1155,"insuranceTypeId":193,"hasSocial":"true","sex":msex,
                             "age":mage,"isApply":"false","applySex":1,"applyAge":18,"idea":-1,"csex":1,
                             "additionalShow":{"zhuyuanRJT":"true","zhuyuanYl":"true","yiwaiYl":"true","yiwaiSh_2":"true"},
                             "years":myears,"baoe1155":10000,"callMethod":1
                             })
    return data


#网络请求
def postdata(opener,urlstr,pama,cookie):
    response = opener.open(urlstr,pama)
    str1 = response.read()
    #cookie.save(ignore_discard=True, ignore_expires=True) #保存cookies
    return str1


if __name__ == "__main__":
    cookiespath = "cookie.txt"
    filename = cookiespath
    cookie = cookielib.MozillaCookieJar(filename)
    cookie.load(cookiespath, ignore_discard=True, ignore_expires=True)  #加载cookies
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    pamasex = [1,2]
    pamaage = 65
    pamayears = [3,5,10]
    lists = []
    for sex in pamasex:
        for i in range(0,pamaage):
            for years in pamayears:
                str1 = postdata(opener,"http://app.winbaoxian.com/planBook/calculate",getp(sex,i,years),cookie)
                print str1
                mresult = json.loads(str1)
                if str(mresult['data']['retcode']) == '0':
                    obj = proplanbaen.ProplanBean(sex,i,years,mresult['data']['outNum']['1155']['baoe'],mresult['data']['outNum']['1155']['baof'])
                    lists.append(obj)
                time.sleep(0.5)
    excel.writevalue(lists)
    print len(lists)

    # str1 = postdata(opener,"http://app.winbaoxian.com/planBook/calculate",getp(1,19,10),cookie)
    #response = opener.open("http://app.winbaoxian.com/planBook/calculate",getp())
    # response1 = opener.open("http://app.winbaoxian.com/user/login/ajaxSave",getlogindata()) #登陆方法
    # print response1.read()
    #result1 = urllib2.urlopen("http://app.winbaoxian.com/main/planbook/ajaxGet?companyId=1")  #获取所有产品
    cookie.save(ignore_discard=True, ignore_expires=True) #保存cookies
    #str1 = response.read()  #只能read()一次

    # print str1
    # mresult = json.loads(str1)

    # obj = proplanbaen.ProplanBean(1,12,3,mresult['data']['outNum']['1155']['baoe'],mresult['data']['outNum']['1155']['baof'])
    # print str1
    # print obj.mbaoe
    #print mresult['data']['retdesc']
