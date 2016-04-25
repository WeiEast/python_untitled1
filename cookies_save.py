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
            'validateCode':'1481'#验证码
        })
    return postdata


def login(opener):
    ###登录
    response1 = opener.open("http://app.winbaoxian.com/user/login/ajaxSave",getlogindata()) #登陆方法
    print response1.read()
    return


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


#保险提交参数3个参数
def getp(msex,mage,myears):
    data = urllib.urlencode({
        "jsonParameters":{"baotype":596,"insuranceTypeId":322,"sex":msex,"age":mage,"isApply":"false","applySex":1,"applyAge":18,"csex":1,
                          "baoImgArr":["yiluyangguang.png"],"additionalShow":{"zhuyuanRe":"true","zhuyuanYl":"true"},
                          "touHmCode":1147,"years":myears,"baoe596":200000,"baoe5961":200000,"baoe5962":200000,"callMethod":1},
        "baotype":596,
        "insuranceTypeId":322,
        "sex":msex,
        "age":mage,
        "isApply":"false",
        "applySex":1,
        "applyAge":18,
        "csex":1,
        "baoImgArr[]":"yiluyangguang.png",
        "additionalShow[zhuyuanRe]":"true",
        "additionalShow[zhuyuanYl]":"true",
        "touHmCode":1147,
        "years":myears,
        "baoe596":200000,
        "baoe5961":200000,
        "baoe5962":200000,
        "callMethod":1,
    })

    return data


#保险提交参数4个参数
def getp4(msex,mage,myears,mduration):
    data = urllib.urlencode({
        "jsonParameters":{"baotype":763,"insuranceTypeId":331,"sex":msex,"age":mage,"csex":1,"baoImgArr":["logo_wyrs.jpg"],
                          "additionalShow":{"zhuyuanRe":"true","zhuyuanYl":"true"},"years":myears,"duration":mduration,"baof605":10000,"callMethod":1},
        "baotype":763,
        "insuranceTypeId":331,
        "sex":msex,
        "age":mage,
        "csex":1,
        "baoImgArr[]":"logo_wyrs.jpg",
        "additionalShow[zhuyuanRe]":"true",
        "additionalShow[zhuyuanYl]":"true",
        "years":myears,
        "duration":mduration,
        "baof605":10000,
        "callMethod":1,
    })
    return data

#网络请求
def postdata(opener,urlstr,pama,cookie):
    response = opener.open(urlstr,pama)
    str1 = response.read()
    #cookie.save(ignore_discard=True, ignore_expires=True) #保存cookies
    return str1


def getvalue():
    pamasex = [1,2]
    pamaminage = 0
    pamaage = 61
    pamayears = [5,10,15,20,30]
    lists = []
    for sex in pamasex:
        for years in pamayears:
            for i in range(pamaminage,pamaage):
                print sex,years,i
                str1 = postdata(opener,"http://app.winbaoxian.com/planBook/calculate",getp(sex,i,years),cookie)
                print str1
                mresult = json.loads(str1)
                if str(mresult['data']['retcode']) == '0':
                    mdict = list()
                    mdict.append(sex)
                    mdict.append(i)
                    mdict.append(years)
                    mdict.append(mresult['data']['outNum']['596']['name'])
                    mdict.append(mresult['data']['outNum']['596']['baoe'])
                    mdict.append(mresult['data']['outNum']['596']['baof'])
                    mdict.append(mresult['data']['outNum']['5961']['name'])
                    mdict.append(mresult['data']['outNum']['5961']['baoe'])
                    mdict.append(mresult['data']['outNum']['5961']['baof'])
                    mdict.append(mresult['data']['outNum']['5962']['name'])
                    mdict.append(mresult['data']['outNum']['5962']['baoe'])
                    mdict.append(mresult['data']['outNum']['5962']['baof'])
                    lists.append(mdict)
                time.sleep(0.2)
    excel.writevalue(lists)
    print len(lists)
    return


def getvalue4():
    pamasex = [1,2]
    pamaminage = 0
    pamaage = 56
    pamayears = [5,10,20]
    duration = [60,65,70]
    lists = []
    for sex in pamasex:
        for years in pamayears:
            for i in range(pamaminage,pamaage):
                for md in duration:
                    print sex,i,years,md
                    str1 = postdata(opener,"http://app.winbaoxian.com/planBook/calculate",getp4(sex,i,years,md),cookie)
                    print str1
                    mresult = json.loads(str1)
                    if str(mresult['data']['retcode']) == '0':
                        mdict = list()
                        mdict.append(sex)
                        mdict.append(i)
                        mdict.append(years)
                        mdict.append(md)
                        mdict.append(mresult['data']['outNum']['605']['name'])
                        mdict.append(mresult['data']['outNum']['605']['baoe'])
                        mdict.append(mresult['data']['outNum']['605']['baof'])
                        lists.append(mdict)
                    time.sleep(0.3)
    excel.writevalue(lists)
    print len(lists)
    return

if __name__ == "__main__":
    cookiespath = "cookie.txt"
    filename = cookiespath
    cookie = cookielib.MozillaCookieJar(filename)
    cookie.load(cookiespath, ignore_discard=True, ignore_expires=True)  #加载cookies
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    # 登录
    #login(opener)
    getvalue()

    cookie.save(ignore_discard=True, ignore_expires=True) #保存cookies

