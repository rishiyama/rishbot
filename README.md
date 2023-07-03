# rishbot

## slackbot

rishbot is the libray for slackbot.


## Installation

Now, the repository is not registered to PyPI. So, you can install it by the following command.
```bash
pip install git+https://github.com/rishiyama/rishbot
```

## ~/.bashrc

Please set the following environment variables to your ~/.bashrc.
SLACK_URL is the url of incoming webhook of slack.
So, You need to set it to your slack channel.
```bash
export SLACK_URL=https://hooks.slack.com/services/x/y/z
```
    
Then, please reload your ~/.bashrc.
```bash
source ~/.bashrc
```



## Usage

Default message is "All finished !!!".

```python
>>> import rishbot as rs
>>> rs.notify_slack()
```
Custom message is also available.
```python
>>> import rishbot as rs
>>> rs.notify_slack("End of the process")
```

## make your version

https://github.com/rishiyama/rishbot/blob/main/rishbot/notify.py
```python
import requests
import os
import json 

# send slack message


def notify_slack(text=f'FIX HERE'):
    requests.post(os.getenv('SLACK_URL'), data=json.dumps({'text': text}))
```
you can change the message by changing the text variable, FIX HERE.