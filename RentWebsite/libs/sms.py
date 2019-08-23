# urllib => 访问URL获取结果
import urllib.request
import urllib
import json
import logging

logger = logging.getLogger('sms')


def send_sms(mobile, captcha):
    # flag用于标记发送短信是否成功，true成功，false失败
    flag = True
    # 这个是短信API地址
    url = 'https://open.ucpaas.com/ol/sms/sendsms'
    # 准备一下头,声明body的格式
    headers = {
        "Content-Type": "application/json; charset=utf-8"
    }
    # 还有我们准备用Post传的值，这里值用字典的形式
    # 从云之讯里面填过来
    values = {
        "sid": "9912e6ddea890c2eecbb352e77b71f29",
        "token": "a4e45e55fe4774efca66d4ec0c262171",
        "appid": "b8e33c80175748feb393d0fc8cd71657",
        # 模板id
        "templateid": "489683",
        # 验证码字符串格式
        "param": str(captcha),
        # 手机号
        "mobile": mobile,
    }
    try:
        # 将字典格式化成bytes格式
        data = json.dumps(values).encode('utf-8')
        logger.info("即将发送短信: {}".format(data))
        # 创建一个request,放入我们的地址、数据、头
        request = urllib.request.Request(url, data, headers)
        # html = '{"code":"000000","count":"1","create_date":"2018-07-23 13:34:06","mobile":"18874933429","msg":"OK","smsid":"852579cbb829c08c917f162b267efce6","uid":""}'
        html = urllib.request.urlopen(request).read().decode('utf-8')
        code = json.loads(html)["code"]
        if code == "000000":
            logger.info("短信发送成功：{}".format(html))
            flag = True
        else:
            logger.info("短信发送失败：{}".format(html))
            flag = False
    except Exception as ex:
        logger.info("出错了,错误原因：{}".format(ex))
        flag = False
    return flag


if __name__ == "__main__":
    # 测试短信接口是否是管用
    send_sms("18874933429", "123456")