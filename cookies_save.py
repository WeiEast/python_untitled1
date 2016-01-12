#coding:utf-8
import cookielib
import urllib2
import urllib
import json

# 验证码登陆
def getlogindata():
    postdata = urllib.urlencode({
            'mobile':'15583581921',
            'validateCode':'7618'
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
def getp():
    data = urllib.urlencode({'jsonParameters':'{"baotype":1155,"insuranceTypeId":193,"hasSocial":true,"sex":1,"age":18,"isApply":false,"applySex":1,"applyAge":18,"idea":-1,"csex":1,"additionalShow":{"zhuyuanRJT":true,"zhuyuanYl":true,"yiwaiYl":true,"yiwaiSh_2":true},"years":10,"baoe1155":10000,"callMethod":1}',
                             "baotype":1155,"insuranceTypeId":193,"hasSocial":"true","sex":2,
                             "age":18,"isApply":"false","applySex":1,"applyAge":18,"idea":-1,"csex":1,
                             "additionalShow":{"zhuyuanRJT":"true","zhuyuanYl":"true","yiwaiYl":"true","yiwaiSh_2":"true"},
                             "years":10,"baoe1155":10000,"callMethod":1
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
    str1 = postdata(opener,"http://app.winbaoxian.com/planBook/calculate",getp(),cookie)
    #response = opener.open("http://app.winbaoxian.com/planBook/calculate",getp())
    #response1 = opener.open("http://app.winbaoxian.com/user/login/ajaxSave",getlogindata()) #登陆方法
    #result1 = urllib2.urlopen("http://app.winbaoxian.com/main/planbook/ajaxGet?companyId=1")  #获取所有产品
    cookie.save(ignore_discard=True, ignore_expires=True) #保存cookies
    #str1 = response.read()  #只能read()一次

    print str1
    mresult = json.loads(str1)
    print mresult['data']['retdesc']
