# Daily Meditation Project

This is a python application that will help users by sending them daily meditation videos that they can access from their email. 

# Setup 
Optionally fork or clone this [repository](https://github.com/ai1196/dailymeditation) that will allow you to create your own copy. You can then proceed to download the remote repository or "clone" it on your local. You can then navigate to where you have downloaded the repo in Terminal.

```
cd ~/desktop/dailymeditation
```

Before proceeding with the environment set up, we need to set up an appropriate email that yagmail can send emails to. Within the desired email account, go to account settings -> security -> ensure 2-step verification is turned on -> app passwords --> select 'Mail' for app type and 'Other' for device type -> after doing so, select 'Generate.' Once the password has been generated, save it somewhere safe! 

To continue the set up, create a virtual environment using Pipenv:
```
pipenv --python 3
```
Install package dependencies within the virtual environment:
```
pipenv install yagmail
```

# Requirements 

Once you have completed the setup steps above, you can continue with the rest of the implementation. 


# Usage
Run the program:
```
pipenv run python runmedprogram.py --username [insert gmail] --app_password $APP_PASSWORD --recipients [insert gmail]
```