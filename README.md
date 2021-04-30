# 老化数据查询平台
* 通过输入IP地址、账户、密码、端口查看平台老化的数据
## Vue安装注意事项
* 切记使用管理员权限运行CMD启动VUE UI
* less-loader版本切记过高维持在7.3.0以下
## Linux部署Python注意事项
* 先执行yum -y install gcc安装gcc编辑器
* 其次执行yum install -y zlib*安装zlib依赖
* 部署Nginx需要修改跨域，实际部署时的跨域是从Nginx处理而不是Node.js中的跨域处理
## 开发过程中的坑点
* cassandra数据查询时使用grep java_cassa是因为通过远程读取的top信息不完整，建议再排查类似问题可以直接查询grep java来确认查询的名字
* Vue解决跨域问题需要修改vue.config.js文件中的内容
* 接口返回值可以存储在sessionStorage中跳转到下一个页面再读取
* 后端接口需要为数组格式
