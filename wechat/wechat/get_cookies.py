# from wechat.free_ip import get_random_proxy
from fake_useragent import UserAgent
import requests

# ua = UserAgent().random
ua = UserAgent(path="./fake_useragent_0.1.11.json")

def get_new_headers():
    headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
              "Accept-Encoding": "gzip, deflate, br",
              "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
              "User-Agent": ua}
    return headers

# def get_new_cookies():
#     url = 'https://v.sogou.com/v?ie=utf8&query=&p=40030600'
#     proxies = {"http": "http://" + get_random_proxy()}
#     headers = {'User-Agent': ua}
#     rst = requests.get(url=url,
#                        headers=headers,
#                        allow_redirects=False,
#                        proxies=proxies)
#     cookies = rst.cookies.get_dict()
#     return cookies

# if __name__ == '__main__':
#     print(get_new_cookies())