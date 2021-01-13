import os
import base64
import pybadges

CURRENT_DIR = os.path.dirname(__file__)
logo_path: str = os.path.join(CURRENT_DIR, 'logo.png')
LOGO: str = "data:image/png;base64," + base64.encodebytes(open(logo_path, 'rb').read()).decode('utf8')

BASE_COLOR: str = '#3FA8FF'


def make_badge(username: str, left_text: str, right_text: str) -> str:
    url = f'https://zenn.dev/{username}'
    return pybadges.badge(left_text=left_text, right_text=right_text, right_color=BASE_COLOR, embed_logo=True, logo=LOGO, left_link=url, right_link=url)
