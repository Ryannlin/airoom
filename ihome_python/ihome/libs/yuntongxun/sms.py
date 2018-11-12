# coding=utf-8

from .CCPRestSDK import REST

# 说明：主账号，登陆云通讯网站后，可在"控制台-应用"中看到开发者主账号ACCOUNT SID
accountSid = '8a216da866e7b2510166e9d6f7f801da'

# 说明：主账号Token，登陆云通讯网站后，可在控制台-应用中看到开发者主账号AUTH TOKEN
accountToken = 'f7d4beea10014506b5891c705a28fcae'

# 请使用管理控制台首页的APPID或自己创建应用的APPID
appId = '8a216da866e7b2510166e9d6f87101e1'

# 说明：请求地址，生产环境配置成app.cloopen.com
serverIP = 'sandboxapp.cloopen.com'

# 说明：请求端口 ，生产环境为8883
serverPort = '8883'

# 说明：REST API版本号保持不变
softVersion = '2013-12-26'

  # 发送模板短信
  # @param to 手机号码
  # @param datas 内容数据 格式为列表 例如：['12','34']，如不需替换请填 ''
  # @param $tempId 模板Id


class CCP(object):
    """自己封装的发送短信的辅助类"""
    # 用来保存对象的类属性
    instance = None

    def __new__(cls):
        # 判断CCP类有没有已经创建好的对象，如果没有，创建一个对象，并且保存
        # 如果有，则将保存的对象直接返回
        if cls.instance is None:
            obj = super(CCP, cls).__new__(cls)

            # 初始化REST SDK
            obj.rest = REST(serverIP, serverPort, softVersion)
            obj.rest.setAccount(accountSid, accountToken)
            obj.rest.setAppId(appId)

            cls.instance = obj

        return cls.instance

    def send_template_sms(self, to, datas, temp_id):
        """"""
        result = self.rest.sendTemplateSMS(to, datas, temp_id)
        # for k, v in result.iteritems():
        #
        #     if k == 'templateSMS':
        #         for k, s in v.iteritems():
        #             print '%s:%s' % (k, s)
        #     else:
        #         print '%s:%s' % (k, v)
        # smsMessageSid:ff75e0f84f05445ba08efdd0787ad7d0
        # dateCreated:20171125124726
        # statusCode:000000
        status_code = result.get("statusCode")
        if status_code == "000000":
            # 表示发送短信成功
            return 0
        else:
            # 发送失败
            return -1


if __name__ == '__main__':
    ccp = CCP()
    ret = ccp.send_template_sms("15811576003", ["1234", "5"], 1)
    print(ret)

    
   
