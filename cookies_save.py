#coding:utf-8
import cookielib
import urllib2
import urllib
import json

# 验证码登陆
def getlogindata():
    postdata = urllib.urlencode({
            'mobile':'15583581921',
            'validateCode':'4734'
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


if __name__ == "__main__":
    cookiespath = "cookie.txt"
    filename = cookiespath
    cookie = cookielib.MozillaCookieJar(filename)
    cookie.load(cookiespath, ignore_discard=True, ignore_expires=True)  #加载cookies
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    response = opener.open("http://app.winbaoxian.com/planBook/calculate",getpama())
    result1 = urllib2.urlopen("http://app.winbaoxian.com/main/planbook/ajaxGet?companyId=1")
    cookie.save(ignore_discard=True, ignore_expires=True) #保存cookies
    print response.read()
    string = response.read()
    mresult = json.loads(string.decode("utf-8"))
#    mresult = json.load(mresult)
    print type(string)
