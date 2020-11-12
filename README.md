# DialogFlow-Python-Client
Google [DialogFlow](logflow.cloud.google.com) Python 3 Client

**Usage**

```console
$ virtualenv venv
$ source venv/Scripts/activate
$ pip install -r requirements.txt
```


Change in <strong>client.py</strong>
1. ``os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'YOUR ACCOUNT CREDENTIALS'``
with your service credential.json file
2. ``DIALOGFLOW_PROJECT_ID = 'YOUR PROJECT NAME'`` with your project name
3. ``DIALOGFLOW_LANGUAGE_CODE = 'en'`` with your language code if it is not english

Run
```shell
$ python3 client.py
```
