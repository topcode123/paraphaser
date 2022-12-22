import json
import requests

url = "https://www.paraphraser.io/frontend/rewriteArticleBeta"

def get_paraphase(paragraph):
    

    payload={'data': paragraph,
    'mode': '1',
    'lang': 'vi',
    'captcha': ''}
    files=[

    ]
    headers = {
    'authority': 'www.paraphraser.io',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': 'ci_session=a%3A6%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%22f0b76de379ae9eabaeeae8d798f43bc3%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A14%3A%22113.190.232.90%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A101%3A%22Mozilla%2F5.0%20%28X11%3B%20Linux%20x86_64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F108.0.0.0%20Safari%2F537.36%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1671673138%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3Bs%3A9%3A%22checkauth%22%3Bs%3A25%3A%22checkparaphrase1671673138%22%3B%7De06cf87029e47d37c57ca687f23eeecf; _ga_Q3XGSV1HE8=GS1.1.1671673139.1.0.1671673139.0.0.0; _ga=GA1.2.1434489752.1671673139; _gid=GA1.2.940584594.1671673140; _gat_gtag_UA_187726107_1=1; _pbjs_userid_consent_data=6683316680106290; _sharedID=599e1cf2-affa-473c-9a66-8eaf70b4b31d; _sharedID_last=Thu%2C%2022%20Dec%202022%2001%3A39%3A00%20GMT; _lr_retry_request=true; _lr_env_src_ats=false; cto_bidid=bXcNQ19rbXpYNTI2Rjd1VmlldmU1dVY5WTRFMEtKYmoxR251UnphTCUyRnFidCUyRk53NU9rdCUyQnY4b0R6OFhXc29kUUE5UzZDUURXdEhCbWpQNEhQZ2clMkJjZTlvdjd1TVZRWHFmeGtzWTZHNjlkWXBOQnNNSnk5aXpHcVNDOEY1dk9aU3JJdldj; __gads=ID=ce5e2375906357fd:T=1671673141:S=ALNI_MZUXbhsmt7Ukx1kcTmbsuVgDRPU-w; __gpi=UID=00000b954af718e4:T=1671673141:RT=1671673141:S=ALNI_Mb_6FSVExiF5Oca7ykGbRc2y6hLzg; lotame_domain_check=paraphraser.io; _cc_id=f6a7b2c401c7592dd4d638a4713cec91; panoramaId_expiry=1672277942486; panoramaId=4f6e603a7900873fc3a9ff355b0416d53938a841ed9eeb52fb1e2be2968bb18a; cto_bundle=m9l38F9yY0pzRU1Vcjh4ZkUlMkJjTEkyWU9FSVRVNk00QWwwVHpmb2N6cktYeHpiU1FuUElsY21INWhicGg4VHhsTzhRT0Z5JTJGb0FCWkxuNXBpWGlWQmZxcjBVazVFcUJQSEs2Wm9hNEYlMkZxQXJGQmlBeHlYcTNmdGJKdnp4QXJzUFRNWlVPbDkzb2NMNHExQ1RaTW41MTlqbWc5aWclM0QlM0Q',
    'origin': 'https://www.paraphraser.io',
    'pragma': 'no-cache',
    'referer': 'https://www.paraphraser.io/vi/cong-cu-giai-thich',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    return json.loads(response.text)
