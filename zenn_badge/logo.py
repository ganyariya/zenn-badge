import os
import base64

CURRENT_DIR = os.path.dirname(__file__)
logo_path: str = os.path.join(CURRENT_DIR, 'logo.png')
LOGO: str = "data:image/png;base64," + base64.encodebytes(open(logo_path, 'rb').read()).decode('utf8')

