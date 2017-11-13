Falconide Python SDK
=================
This is the official Falconide SDK for Python. 

This SDK uses the Requests library and will work for Python 2.6 — 3.5.

INSTALLATION: 
=============
```shell
git clone https://github.com/falconide/falconide-sdk-python.git .
cd falconide-sdk-python
sudo pip install -r requirements.txt
```

Usage Example:
===========
Edit example.py, as per your requirements

```python
from falconideapiv10.falconideapiv_10_client import Falconideapiv10Client
client = Falconideapiv10Client()
email_client = client.email

data = { 
    'api_key' : 'yoursecretapikey',
    'recipients' : ['recipient1@example.com','recipient2@example.com'],
    'email_details' : { 
        'fromname' : 'sender name',
        'subject' : 'test email subject sent using Falconide SDK - Python',
        'from' : 'from@example.com',
        'content' : '<p>This is a test email sent using Falconide JSON/Email Python SDK</p>'
    }   
}

res = email_client.create_falconapi_web_send_json(data)

print res
```

Advance Usage Example:
===========
Edit example.py, as per your requirements

```python
from falconideapiv10.falconideapiv_10_client import Falconideapiv10Client
client = Falconideapiv10Client()
email_client = client.email

data = {
    'api_key': 'yoursecretkey',
    'recipients': ['recipient1@example.com', 'recipient2@example.com'],
    'recipients_cc' : ['recipient1@example.com','recipient2@example.com'],	
    'email_details': {
        'from': 'from@example.com',
        'subject': 'Hi [% NAME %], here is your account balance.',
        'content': '<p>Hi [%NAME%],<\/p><p>Your account balance is [% ACCOUNT_BAL %].<\/p>',
        'fromname': 'SDK Sender Name ',
        'replytoid': 'replyto@example.com'
    },
    'tags': 'AccountDeactivation, Verification',
    'X-APIHEADER': ['UserID1', 'UserID2'],
    'X-APIHEADER_CC': ['UserID6', 'UserID7'],
    'settings': {
        'footer': true,
        'clicktrack': true,
        'opentrack': true,
        'unsubscribe': true,
        'bcc': 'bcc@example.com',
        'attachmentid': '1,2,3',
        'template': '101',	
    },
    'attributes': {
        'NAME': ['NameOfRecipient1', 'NameOfRecipient2'],
        'ACCOUNT_BAL': ['100', '200']
    },
    'files': {
        'example_attachment1.txt': '', # Get Binary content of file and encode by base64
        'example_attachment2.pdf': ''
    }
} 
res = email_client.create_falconapi_web_send_json(data)

print res
```

Run the script
```shell
python example.py
```

This SDK was semi-automatically generated by APIMATIC v2.0. Thanks to [APIMATIC](http://apimatic.io/)



