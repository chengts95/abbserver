#基于MQTT的物联网医疗监护平台原型

基于MQTT的物联网平台的原型展示。

本仓库包含我根据HKB-08B臂式血压计模块的通讯协议写的python通讯协议库:`srtp/bpr.py`, 基于此库  
建立了MQTT上位机程序：`srtp/hardware_client.py`可用于树莓派上构成网络血压计，作为监控平台的  
测试硬件。同时也有开发调试时用的虚拟血压计客户端：`srtp/virutal_client.py`,服务端数据采集程  
序：`srtp/broker.py`。 在`web`文件夹中是服务端后台程序，提供restful API以及websocket端口，可查询  
最新血压测量结果。`web/restful.py`即是服务器后台程序。
