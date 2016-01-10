import urllib2
import urllib
import excel
import json
import cookielib
from Cookie import SimpleCookie


def build_opener_with_cookie_str(cookie_str, domain, path='/'):
    simple_cookie = SimpleCookie(cookie_str)    # Parse Cookie from str
    cookiejar = cookielib.CookieJar()    # No cookies stored yet

    for c in simple_cookie:
        cookie_item = cookielib.Cookie(
            version=0, name=c, value=str(simple_cookie[c].value),
                     port=None, port_specified=None,
                     domain=domain, domain_specified=None, domain_initial_dot=None,
                     path=path, path_specified=None,secure=None,expires=None,discard=None,
                     comment=None,comment_url=None,rest=None,rfc2109=False,
            )
        cookiejar.set_cookie(cookie_item)    # Apply each cookie_item to cookiejar
        print c+str(simple_cookie[c].value)
    return urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))    # Return opener


if __name__=="__main__":
    url="http://app.winbaoxian.com/planBook/calculate"
    url1 = "http://www.5rc.com.cn/chinalifeweb/j_spring_security_check"
    sc = SimpleCookie('JSESSIONID=83979F6CEA5BBE6BFDC106869E429071;SERVERID:0566107f0b6ad539dab2d166a3543cea|1452416678|1452416672;token:9730a1acea474f259f0ef080f9de7a38')
    cookie_str = 'JSESSIONID=83979F6CEA5BBE6BFDC106869E429071;' \
                 'SERVERID=0566107f0b6ad539dab2d166a3543cea|1452416678|1452416672;' \
                 'token=9730a1acea474f259f0ef080f9de7a38;' \
                 'Hm_lpvt_59c99e4444d9fb864780844a90b61aea=1452416664;' \
                 'Hm_lvt_59c99e4444d9fb864780844a90b61aea=1452254134,1452390064,1452416661'
    opener = build_opener_with_cookie_str(cookie_str, domain='http://app.winbaoxian.com')

    html_doc = opener.open(url).read()
    print html_doc
    # values = {'insuranceTypeId':'168','sex':'1','age':"18",'years':"10",'baoe':"10",'baofei':"4113",'idea':"-1",'cname':"",'csex':"1"}
    # # response = urllib2.urlopen("http://app.winbaoxian.com/main/planbook/ajaxGet?companyId=1")
    #
    # user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0'
    #
    # data = urllib.urlencode(values)
    # headers = { 'User-Agent' : user_agent }
    # request = urllib2.Request(url, data)
    # cookie = cookielib.MozillaCookieJar()
    #
    # urllib2.build_opener(urllib2.HTTPCookieProcessor(sc))
    # calresponse  = urllib2.urlopen(request)
    #encodejson = json.dumps(responsfe.read())


