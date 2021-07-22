import subprocess
import requests

urls = ["https://www.google.com/", "https://www.linkedin.com/"]

appleScriptCommand = '''
on run argv
  display notification (item 2 of argv) with title (item 1 of argv)
end run
'''

def notify(title, text):
  subprocess.call(['osascript', '-e', appleScriptCommand, title, text])

def url_health_check(url_list):
    notification_message = ""
    for url in url_list:
        r = requests.get(url)
        if str(r.status_code) != "200":
            notification_message += str(r.status_code) + "  " + url + "\n"
            notify("Site Health Check Alert", notification_message)

url_health_check(urls)