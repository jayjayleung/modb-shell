# modb-shell
【墨天轮】python脚本自动签到 【墨天轮】https://www.modb.pro/

## 使用
1. [Fork 仓库](https://github.com/iDerekLi/juejin-helper)

2. 仓库 -> Settings -> Secrets -> New repository secret, 添加Secrets变量如下:

    | Name | Value | Required |
    | --- | --- | --- |
    | COOKIE | 墨天轮网站Cookie  | 是 |
    | COOKIE_2 | 多用户, 当需要同时运行多个墨天轮用户时所需, 支持最多 **5** 名用户(即COOKIE + COOKIE_2 - COOKIE_5)  | 否 |
    | PUSHPLUS_TOKEN | [Pushplus](http://www.pushplus.plus/) 官网申请，支持微信消息推送 | 否 |

3. 仓库 -> Actions, 检查Workflows并启用。
