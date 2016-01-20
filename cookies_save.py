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
            'validateCode':'2067'#验证码
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
        "jsonParameters":{"baotype":5031,"insuranceTypeId":74,"hasSocial":"true","sex":str(msex),"age":str(mage),"isApply":"false","applySex":1,"applyAge":18,"idea":-1,"csex":1,"additionalShow":{"zhuyuanRJT":"true","zhuyuanYl":"true","yiwaiYl":"true","yiwaiSh_2":"true"},"level":2,"years":str(myears),"account":0,"baof5031":10000,"callMethod":1},
        "baotype":5031,"insuranceTypeId":74,"hasSocial":"true","sex":str(msex),"age":str(mage),"isApply":"false","applySex":1,"applyAge":18,"idea":-1,"csex":1,
        "additionalShow[zhuyuanRJT]":"true","additionalShow[zhuyuanYl]":"true","additionalShow[yiwaiYl]":"true","additionalShow[yiwaiSh_2]":"true",
        "level":2,"years":str(myears),"account":0,"baof5031":10000,"callMethod":1
    })
    return data


#保险提交参数4个参数
def getp4(msex,mage,myears,mduration):
    data = urllib.urlencode({
        "jsonParameters":{"baotype":28,"insuranceTypeId":218,"hasSocial":"true","sex":str(msex),"age":str(mage),"isApply":"false","showApply":"true","applySex":1,"applyAge":20,"idea":-1,"csex":1,"baoeToBaof":"false","cover":3,"takePopupArr":[],"additionalShow":{"laolaiF":"true","shaonianZ":"true"},"years":str(myears),"duration":str(mduration),"baof034":10000,"callMethod":1},
        "baotype":28,"insuranceTypeId":218,"hasSocial":"true","sex":str(msex),"age":str(mage),"isApply":"false","showApply":"true","applySex":1,"applyAge":20,"idea":-1,"csex":1,
        "baoeToBaof":"false","cover":3,"additionalShow[laolaiF]":"true","additionalShow[shaonianZ]":"true","years":str(myears),"duration":str(mduration),"baof034":10000,"callMethod":1

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
    pamaage = 59
    pamayears = [1,3,5,10,15,20]
    lists = []
    for sex in pamasex:
        for years in pamayears:
            for i in range(pamaminage,pamaage):
                str1 = postdata(opener,"http://app.winbaoxian.com/planBook/calculate",getp(sex,i,years),cookie)
                print str1
                mresult = json.loads(str1)
                if str(mresult['data']['retcode']) == '0':
                    obj = proplanbaen.ProplanBean(sex,i,years,mresult['data']['outNum']['5031']['baoe'],mresult['data']['outNum']['5031']['baof'])
                    lists.append(obj)
                time.sleep(0.5)
    excel.writevalue(lists)
    print len(lists)
    return


def getvalue4():
    pamasex = [1,2]
    pamaminage = 0
    pamaage = 60
    pamayears = [3,5,10,20]
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
                        obj = proplanbaen.ProplanBean(sex,i,years,mresult['data']['outNum']['034']['baoe'],mresult['data']['outNum']['034']['baof'])
                        lists.append(obj)
                    time.sleep(0.5)
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
    # login(opener)
    getvalue4()

    cookie.save(ignore_discard=True, ignore_expires=True) #保存cookies

