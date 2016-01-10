import urllib2
import json
response = urllib2.urlopen("http://app.winbaoxian.com/main/planbook/ajaxGet?companyId=1")
encodejson = json.dumps(response.read())
print encodejson[0]