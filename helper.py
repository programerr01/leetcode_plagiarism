import cloudscraper
import time
from config import RETRIES,RETRIES_PAGE
requests = cloudscraper.CloudScraper();




headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version-list': '"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.182", "Google Chrome";v="126.0.6478.182"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
cookies = {
    'csrftoken':'CiezlMc9xA10sEth2NaRm3yBNaKuNSMp8GlJ4TPynvJ27TcqJsROE8F2CiWKJfWh',
    '__cf_bm':"s_G_QoL.xBL24UoLy8H7kmZQciX20HvCMMsAacNnOf4-1728401570-1.0.1.1-rEEL9XZBEPyB975x8Y2h2HDADliiOwiJgyYCyUBqqHt9gdAGW.95bsoQM9UT1w1_ab__26CAxWeawAD3wnBndQ",
    'ip_check': '(false, "110.74.221.118")',
    '_gid': 'GA1.2.1006983287.1728403098',
    '_gat': '1',
    '_ga': 'GA1.1.1852366448.1728403098',
    '_ga_CDRWKZTDEX': 'GS1.1.1728403098.1.0.1728403098.60.0.0',
    'gr_user_id': '9a9997eb-de75-49de-a3b3-230cbebf7510',
    '87b5a3c3f1a55520_gr_session_id': '358cd367-378d-4bb2-bd2c-bf4646e76284',
    '87b5a3c3f1a55520_gr_session_id_sent_vst': '358cd367-378d-4bb2-bd2c-bf4646e76284',

}

def get_contest_details(isWeekly,contest_id):
    global cookies
    typ = "biweekly-contest-" if not isWeekly else "weekly-contest-"
    url_ = f"https://leetcode.com/contest/api/info/{typ}{contest_id}/"
    print(url_)    
    for i in range(RETRIES):
        res = requests.get(url_,cookies=cookies)
        if(res.status_code == 200):
            return res;
        cookie = res.cookies;
        csrf = cookie.get("csrftoken") 
        cf_bm = cookie.get("__cf_bm")
        cookies['csrftoken'] = csrf if csrf else ""
        cookies['__cf_bm'] = cf_bm if cf_bm else ""
        if(i == RETRIES-1):
            return res; 
        time.sleep(2)



def get_page_ranking(isWeekly,contest_id,page_no):
    global cookies
    typ = "biweekly-contest-" if not isWeekly else "weekly-contest-"
    url_ = f"https://leetcode.com/contest/api/ranking/{typ}{contest_id}/?pagination={page_no}&region=global_v2"
    print(url_)    
    for i in range(RETRIES_PAGE):
        res = requests.get(url_,cookies=cookies)
        if(res.status_code == 200):
            return res;
        cookie = res.cookies;
        csrf = cookie.get("csrftoken") 
        cf_bm = cookie.get("__cf_bm")
        cookies['csrftoken'] = csrf if csrf else ""
        cookies['__cf_bm'] = cf_bm if cf_bm else ""
        if(i == RETRIES-1):
            return res; 
        time.sleep(2)


def get_user_submission(submission_id,is_china_server):
    global cookies
    domain  = "cn" if is_china_server else "com"
    url_  = f"https://leetcode.{domain}/api/submissions/{submission_id}/"
    for i in range(RETRIES):
        res = requests.get(url_,headers=headers,cookies=cookies)
        if(res.status_code == 200):
            return res;
        cookie = res.cookies;
        csrf = cookie.get("csrftoken")
        cf_bm = cookie.get("__cf_bm")
        cookies['csrftoken'] = csrf if csrf else cookies['csrftoken']
        cookies['__cf_bm'] = cf_bm if cf_bm else cookies['__cf_bm']
        if(i == RETRIES-1):
            return res;
        time.sleep(2)
    return res


