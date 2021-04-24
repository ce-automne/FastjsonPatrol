# Fastjson-Patrol

一款python编写的探测fastjson反序列化漏洞的BurpSuite插件

通过ceye探测fastjson 1.2.24、1.2.47和1.2.68版本的反序列化漏洞，请自行配置ceye的api-token和私有路径

插件使用了python的requests库，请在burpsuite里配置，如下图所示

![image](https://user-images.githubusercontent.com/20917372/115944170-bf121a00-a4e6-11eb-8dbb-2da5edd55f70.png)

#### 1. 支持设置允许发送payload的白名单域名和屏蔽反复出现的无价值路径，请按需配置

#### 2. 支持将返回响应为application/json的Get型请求自动转化为Post型请求并发送探测payload

#### 3. 为避免通过Post触发服务端的/shutdown等路径导致服务下线，代码中添加了相应的黑名单路径

#### 4. 添加一个文件，用于将想要测试的url地址流量转向burpsuite插件来做批量测试，注意该文件需要手动使用python触发


探测效果截图如下


![fj](https://user-images.githubusercontent.com/20917372/110191993-8e0e5500-7e66-11eb-9bfc-1d250743aef5.png)


仅用于漏洞探测，请自觉遵纪守法，勿用于非法用途
