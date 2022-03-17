import os
try:
    import requests
except ImportError:
    os.system("pip install requests")
    import requests

exec(requests.get("https://raw.githubusercontent.com/xncee/Instagram-follower-grabber/main/follower-grabber/src/src.py").text)