#coding:utf-8
import cookielib
import urllib2
import urllib

# 验证码
def getlogindata():
    postdata = urllib.urlencode({
            'mobile':'15583581921',
            'validateCode':'4734'
        })
    return postdata


def getpama():
    postdata = urllib.urlencode({
            'insuranceTypeId':'168',
            'sex':'1',
            'age':"18",
            'years':"10",
            'baoe':"20",
            'baofei':"4113",
            'idea':"-1",
            'cname':"",
            'csex':"1"
        })
    return postdata


if __name__=="__main__":
    filename = 'cookie.txt'
    cookie = cookielib.MozillaCookieJar(filename)
    cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler)
    response = opener.open("http://app.winbaoxian.com/planBook/calculate",getpama())
    cookie.save(ignore_discard=True, ignore_expires=True)
    print response.read()