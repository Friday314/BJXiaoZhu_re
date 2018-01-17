import requests
import re

# 请求头文件
_headers = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
}

res = requests.get("https://bj.xiaozhu.com/", headers=_headers)

prices = re.findall('<span class="result_price">&#165;<i>(.*?)</i>起/晚</span>', res.text)

for price in prices:
    print(price)

