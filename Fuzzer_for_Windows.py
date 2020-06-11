from tqdm import tqdm
import sys
import requests
from colorama import init
init()

status_codes = {100:"\033[1;32;40mContinue \033[1;37;40m",200:"\033[1;32;40mCan Resolve Host \033[1;37;40m",101:"Switching Protocols",102:"Processing (WebDAV"
        ,203:"Non-Authoritative Information",201:"Created",202:"\033[1;32;40mAccepted\033[1;37;40m",204:"\033[1;31;40mNo Content\033[1;37;40m",
        205:"\033[1;33;40mReset Content\033[1;37;40m",206:"\033[1;32;40mPartial Content\033[1;37;40m",207:"Multi-Status (WebDAV)",
        208:"\033[1;33;40mAlready Reported (WebDAV\033[1;37;40m)",226:"IM Used",300:"\033[1;33;40mMultiple Choices\033[1;37;40m",
        301:"\033[1;33;40mMoved Permanently\033[1;37;40m",302:"\033[1;33;40mFound\033[1;37;40m",303:"\033[1;33;40mSee Other\033[1;37;40m",304:"\033[1;33;40mNot Modified\033[1;37;40m",
        305:"\033[1;33;40mUse Proxy\033[1;37;40m",307:"\033[1;33;40mTemporary Redirect",308:"\033[1;33;40mPermanent Redirect (experimental)",
        400:"\033[1;31;40mBad Request\033[1;37;40m",401:"\033[1;31;40mUnauthorized",402:"Payment Required",403:"\033[1;31;40mForbidden",
        404:"\033[1;31;40mNot Found\033[1;37;40m",405:"\033[1;31;40mMethod Not Allowed",406:"\033[1;31;40mNot Acceptable",407:"\033[1;31;40mProxy Authentication Required",
        408:"\033[1;31;40mRequest Timeout\033[1;37;40m",409:"\033[1;31;40mConflict",410:"\033[1;31;40mGone",411:"\033[1;31;40mLength Required",412:"\033[1;31;40mPrecondition Failed",
        413:"Request Entity Too Large",414:"Request-URI Too Long",415:"Unsupported Media Type",
        416:"Requested Range Not Satisfiable",417:"Expectation Failed",418:"I'm a teapot (RFC 2324",
        420:"\033[1;31;40mEnhance Your Calm (Twitter)\033[1;37;40m",422:"Unprocessable Entity (WebDAV)",423:"\033[1;31;40mLocked (WebDAV)\033[1;37;40m",
        424:"\033[1;31;40mFailed Dependency (WebDAV)\033[1;37;40m",425:"Reserved for WebDAV",426:"Upgrade Required",
        428:"\033[1;31;40mPrecondition Required\033[1;37;40m",429:"\033[1;31;40mToo Many Requests\033[1;37;40m",431:"\033[1;31;40mRequest Header Fields Too Large",
        444:"\033[1;31;40mNo Response (Nginx)\033[1;37;40m",449:"\033[1;31;40mRetry With (Microsoft)",
        450:"BLocked by Windows Parental Controls (Windows)",451:"Unavailable For Legal Reasons",
        499:"\033[1;31;40mClient Closed Request (Nginx)\033[1;37;40m",500:"Internal Server Error",501:"Not Implemented",
        502:"\033[1;31;40mBad Gateway\033[1;37;40m",503:"Service Unavailable",504:"Gatewat Timeout",505:"HTTP Version Not Supported",
        506:"Variant Also Negotiates",507:"Insufficient Storage",508:"Loop Detected (WebDAV)",
        509:"Bandwidth Limit Exceeded (Apache)",510:"Not Extended",511:"Network AUthentication Required",
        598:"Network read timeout error",599:"Network connect timeout error"}

def webpage(wordlist, url):
    pages = 0
    r = requests.get(url)
    #if r.status_code == 200:
    for index in tqdm(wordlist):
        pass
        new_url = url.replace("FUZZ",index)
        page = requests.get(new_url)
        status = page.status_code
        for i in status_codes:
            if status == i:
                if i == 404:
                    pass
                else:
                    pages += 1
                    msg = "{} : {}".format(new_url,status_codes[i])
                    tqdm.write(msg)
    if pages == 0:
        print("Nothing Found")
    else:
        print("#" * 80)
        print("Finished :) - Feel free to follow me on Twitter @A_L_E_X_H_A_L_L")
        print("#" * 80)
                    


def wordlist(wordlist, url):
    url = url
    with open(wordlist, "r") as wordlist_:
        word_list = []
        for index in wordlist_:
            word_list.append(index.strip())
    webpage(word_list, url)
      





def main(user_input):
    print("#" * 60)
    print("#" * 60)
    print("\n")
    print(r""" _       __     __         _ __          ______                         
| |     / /__  / /_  _____(_) /____     / ____/_  __________  ___  _____
| | /| / / _ \/ __ \/ ___/ / __/ _ \   / /_  / / / /_  /_  / / _ \/ ___/
| |/ |/ /  __/ /_/ (__  ) / /_/  __/  / __/ / /_/ / / /_/ /_/  __/ /    
|__/|__/\___/_.___/____/_/\__/\___/  /_/    \__,_/ /___/___/\___/_/     
                                                                        
    ______              _       ___           __                  
   / ____/___  _____   | |     / (_)___  ____/ /___ _      _______
  / /_  / __ \/ ___/   | | /| / / / __ \/ __  / __ \ | /| / / ___/
 / __/ / /_/ / /       | |/ |/ / / / / / /_/ / /_/ / |/ |/ (__  ) 
/_/    \____/_/        |__/|__/_/_/ /_/\__,_/\____/|__/|__/____/  Version 1.0""")
    print("\n")
    print("Twitter: @A_L_E_X_H_A_L_L")
    print("#" * 60)
    print("#" * 60)
    if len(user_input) == 1:
        tqdm.write("\nUsage: python fuzzer.py http://URL PATH_TO_WORDLIST \n")
    else:
        tqdm.write("\nUsage: python fuzzer.py http://URL PATH_TO_WORDLIST \n")
        file = user_input[2]
        webpage = user_input[1]
    wordlist(file,webpage)
        

main(sys.argv)


                                                      
