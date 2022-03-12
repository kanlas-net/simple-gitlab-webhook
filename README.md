# Simple Gitlab Webhook
Simple http server which checks incoming request for X-Gitlab-Token header and validates its value to run specified local file. To run server you need only python3 installed, any additional dependencies aren't needed. 


Typical usage:
```bash
python3 webhook.py -x /path/to/my/exec/file -s my_secret
```
You can specify another IP, port and header:
```bash
python3 webhook.py -l 127.0.0.2 -p 1313 -H 'My-Custom-Header' -x /path/to/my/exec/file -s my_secret
```
