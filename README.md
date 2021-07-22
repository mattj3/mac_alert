# macAlert

## References
- https://stackoverflow.com/questions/17651017/python-post-osx-notification

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