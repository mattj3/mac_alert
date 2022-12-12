# macAlert
Simple script to produce a macOS alert (banner) if a provided url does not give a 200 response. 
Pair with crontab to automate checks. 

## References
- stackoverflow dot com slash questions slash 17651017 slash python-post-osx-notification

## Feature Improvement Ideas 
- Add audible alert 
- Containerize/playbook (python3, pip3, subprocess, requests)
- Linux version
- Add in `str(r.elapsed.total_seconds())` for longer 200 responses

## Optional 
```
#Use below if you want an alert even if there are no issues, can be annoying if running frequently -MJ
if (notification_message == ""):
    notification_message = "No issues found! Get some coffee!"
```
