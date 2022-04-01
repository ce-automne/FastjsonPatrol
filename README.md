## Fastjson-Patrol

一款python编写的探测fastjson反序列化漏洞的BurpSuite插件  
通过ceye探测fastjson 1.2.24、1.2.47和1.2.68版本的反序列化漏洞，请自行配置ceye的api-token和私有路径

① 注册登录ceye.io平台后，使用**私有路径**替换掉FastjsonPatrol.py代码里如下图所示的xxxx字符串，注意Payload24/Payload47/Payload68_1/Payload68_2/Payload68_3这几个变量都要替换
![image](https://user-images.githubusercontent.com/20917372/161260412-dfe3aee6-b8eb-430d-836d-0547ab177c77.png)

②另外使用**api-token**替换掉FastjsonPatrol.py代码的如下图标记处即可  
![image](https://user-images.githubusercontent.com/20917372/161261286-6c63bea3-a258-463e-8391-6c1090eee92e.png)  

③ 为了有针对性地扫描，程序只会对whitedomains里配置的**域名结尾**的资产以及**ip资产**进行漏洞探测，blackuris里用于配置不进行漏洞探测的url路径关键词  
![image](https://user-images.githubusercontent.com/20917372/161261772-7a91d278-9e34-4329-885a-d6a2a97e9f3b.png)  

![image](https://user-images.githubusercontent.com/20917372/161263122-1ca82a54-9319-4b53-b9dc-f66d458b97ed.png)


## 插件安装

插件使用了python的requests库，请在BurpSuite里配置，如下图所示
```
pip install requests==2.21.0
```

![image](https://user-images.githubusercontent.com/20917372/115944170-bf121a00-a4e6-11eb-8dbb-2da5edd55f70.png)


## 说明

1. 支持设置允许发送payload的白名单域名和屏蔽反复出现的无价值路径，请按需配置
2. **支持将返回响应为application/json的Get型请求自动转化为Post型请求并发送探测payload**
3. 为避免通过Post触发服务端的/shutdown等路径导致服务下线，代码中添加了相应的黑名单路径
4. 添加了send2fastjsonPatrol.py文件，用于将想要测试的url地址流量转向burpsuite插件来做批量测试，注意该文件需要手动使用python触发

## 插件使用效果

![image](https://user-images.githubusercontent.com/20917372/110191993-8e0e5500-7e66-11eb-9bfc-1d250743aef5.png)

## 免责声明

仅作为技术研究，请自觉遵纪守法，勿用于非法用途
