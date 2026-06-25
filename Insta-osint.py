import requests,bs4,json
red = "\033[1m\033[31m"
green = "\033[1m\033[32m"
yellow = "\033[1m\033[33m"
blue = "\033[1m\033[34m"
cyan = "\033[1m\033[36m"
magenta = "\033[1m\033[35m"
white = "\033[1m\033[37m"
reset="\033[0m"
def insta_profile(username:str,choice:int):
    result={}
    url=f'https://www.instagram.com/api/v1/users/web_profile_info/?username={username}'
    header={
  "x-ig-app-id": "936619743392459",
  "accept": "*/*",
  "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36",
  "referer": "https://www.instagram.com/ankubyte",
  "accept-encoding": "gzip, deflate, br, zstd",
  "accept-language": "en-US,en;q=0.9",
    }
    req=requests.get(url=url,headers=header)

    stcode=req.status_code
    if stcode!=200:
        result["error"]= f"Error occured:\nStatus Code: {stcode}\n"
    else:
        # res
        res=req.json()
        if choice==1:
            user=res['data']['user']
            result={
                "Message" : f"✅ Profile Info...",
                "Data":{
                    "Full Name": user["full_name"],
                    "username": user["username"],
                    "Id": user["id"],
                    "Business Account": user["is_business_account"],
                    "Creator Account": user["is_professional_account"],
                    "Biography": user["biography"],
                    "Bio Link": user["external_url"],
                    "Follower":user["edge_follow"]["count"],
                    "Following":user["edge_followed_by"]["count"],
                    "Category Name": user["category_name"],
                    "Media Count":user["edge_owner_to_timeline_media"]["count"],
                    "Profile Pic":user["profile_pic_url_hd"]
                     }

                    }
        else:
            with open('insta_profile.json','w',encoding='utf-8') as f:
                    json.dump(res, f, ensure_ascii=False, indent=2)
            result["Message"]=f"⛔️Full Profile analyze\n and Saved as inta_profile.json"
    return result

def main():
    print(f'{yellow}Welcome to Insta Profile Analyzer')
    print(f'{reset}=+'*50)
    username=input(f'{cyan}Enter Username: {reset}').strip()
    print(f'{red}Please Choose :\n{reset}[+]{reset}{yellow}1:{reset}Basic Profile info\n{reset}[+]{reset}{yellow}2:{reset}advance Profile info')
    
    choic=int(input("Enter 1/2:"))
    data=insta_profile(username,choic)
    for k, y in data.items():
        if isinstance(y, dict):
            print(f"\n{cyan}{k}:{reset}")
            for k2, y2 in y.items():
                print(f"   {yellow}{k2}{reset} = {y2}")
        else:
            print(f"{cyan}{k}{reset} = {y}")

main()
    




