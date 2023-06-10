import jwt
import datetime

# 加的盐

JWT_SALT = "ds()udsjo@jlsdosjf)wjd_#(#)$"


def create_token(payload):
    # 声明类型，声明加密算法
    headers = {
        "type": "jwt",
        "alg": "HS256"
    }
    # 设置过期时间
    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(days=30)
    result = jwt.encode(payload=payload, key=JWT_SALT, algorithm="HS256", headers=headers).decode("utf-8")
    # 返回加密结果
    return result


def parse_payload(token):
    """
    用于解密
    :param token:
    :return:
    """
    result = {"status": True, "data": None}
    try:
        # 进行解密
        verified_payload = jwt.decode(token, JWT_SALT, True)
        result['data'] = verified_payload
        print(verified_payload)
    except Exception as e:
        result['status'] = False

    return result
