# Fastjson-Patrol

一款探测fastjson漏洞的Burpsuite插件

通过ceye探测fastjson 1.2.24、1.2.47和1.2.68版本的反序列化漏洞

支持设置允许发送payload的白名单域名和屏蔽反复出现的无价值路径

支持将返回响应为application/json的Get型请求自动转化为Post型请求并发送探测payload
