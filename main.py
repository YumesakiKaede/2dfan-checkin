import json
import os
from typing import Optional
from api import User
from recaptcha import EzCaptchaImpl

sessions = os.environ.get(key='in20wlbwGbYq6ypbF9hKm8yOTXPGjaJJ2BoBGv7AUi6izdc4SOh7v9eurfvVnIhqND%2FOjJTP0Dp4ZLS%2BoBGv7AUi6izdc4SOh7v9eurfvVnIhqND%2FOnsSP0Dp4Dm8Fe3LDITuT7jK22BJw%3D%3D%2BLvk9fyqPYzERwKA--tiCNbvdFadszITuT7IK%2BJw%3D%3D%2BLvk9fyqPYzERwKA--tiCNbvdFadszITuT7IK%2BJw%3D%3D%2BLvk9fyqPYzERwKA--tiCNbvdFadszITuT7IK%2BJw%3D%3D%2BLvk9fyqPYzERwKA--tiCNbvdFadszITuT7IK%2BJw%3D%3D%2BLvk9fyqPYzERwKA--tiCNbvdFadszITuT7IK%2BJw%3D%3D', default='').split(',')
session_map_str: Optional[str] = os.environ.get(key='SESSION_MAP', default=None)
if not session_map_str:
    raise EnvironmentError("缺少环境变量 SESSION_MAP")
session_map: dict[str, str] = json.loads(session_map_str)
http_proxy: str = os.environ.get(key='HTTP_PROXY', default=None)

if __name__ == '__main__': 
    print("begin checkin")
    for key in session_map.keys():
        session = session_map[key]
        user = User(key, session, EzCaptchaImpl())
        if http_proxy:
            user.session.proxies.update({
                'http': http_proxy,
                'https': http_proxy,
            })
        print('session:',session[:3], '签到结果:', user.checkin().__dict__) 
        # print(user.get_authenticity_token())
    print("finish checkin")
