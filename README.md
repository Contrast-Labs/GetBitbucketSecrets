# GetBitbucketSecrets.py

Recover all Bitbucket pipeline variables and secrets available to a user in a target organization. This includes secrets the user is permitted to access, such as AWS credentials, along with variables that has not been properly secured. 


## Example:
```
python3 GetBitbucketSecrets.py -t exampleorg -u exampleuser -p examplepassword
```

Note that if the Bitbucket account has 2fa enables, an [App Password](https://bitbucket.org/account/settings/app-passwords/) (Personal Settings > App passwords) is required.

Creating a new App Password is not opsec safe, and will send an email notification to the user email address. 

# Usage
```
usage: GetBitbucketSecrets.py -t exampleorg -u exampleuser -p examplepassword

Extract BitBucket Pipeline Variables - @DanAmodio

optional arguments:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        Target Bitbucket org name
  -u USERNAME, --username USERNAME
                        Login Username (Personal settings > Account settings >
                        Username)
  -p PASSWORD, --password PASSWORD
                        Login Password or App Password if 2fa (Personal
                        settings > App passwords)
  -d, --debug           Enable debug logging
  -o {default,csv}, --output {default,csv}
                        Output format
```

