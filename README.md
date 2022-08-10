# Daily Meditation Project

This is a python application that will help users by sending them daily meditation videos that they can access from their email. 

# Setup 
Optionally fork or clone this [repository](https://github.com/ai1196/dailymeditation) that will allow you to create your own copy. You can then proceed to download the remote repository or "clone" it on your local. 

Before proceeding with the environment set up, we need to set up an appropriate email that yagmail can send emails to. Within the desired email account, go to:
+ Account Settings
+ Select Security
+ Ensure 2-step verification is turned on
+ Select App Passwords
+ Under App Passwords, select 'Mail' for app type and 'Other' for device type
+ After doing so, select 'Generate.' 
+ Once the password has been generated, save it somewhere safe! 

To continue the set up, create a virtual environment using Pipenv:
```
pipenv --python 3
```
Install package dependencies within the virtual environment:
```
pipenv install yagmail
```
To activate this project's virtualenv, run:
```
pipenv shell
```
You can then navigate to where you have downloaded the repo in Terminal.

```
cd ~/desktop/dailymeditation
```
Export password with:
```
export APP_PASSWORD='enter password'
```

# Requirements 

Once you have completed the setup steps above, you can continue with the rest of the implementation. 

## Passing in User Details

We'll need to identify a way to pass in user details (i.e. user email and password). The application should be able to ingest the user's email and password so that we can ensure the medication email gets sent to the user. 

## Meditation Asset Format 

Next, we'll need to get the name and url of the meditation assets and format it in html since the email will be rendered as html.

We'll also want to include a series of videos and their corresponding URLs so that it makes it easy for the user to access.

## Identifying Routine Format

Once we have passed in the user details and creating the meditation format, we can move on to creating the routine. 

The routine will need to include both a series of exercises and a subset of those exercises for the videos that will be attributed to a particular day. 

We expect that in the email, the user should be able to see:
+ Name of Meditation 
+ See the Meditation 
+ List of Meditation Videos

## Create a Warm Up Message

Then, we'll need to create a friendly warm up message and embed a video that the user can select to get started on meditation warm up. 

## Implementating the Meditation Program

We'll need to ensure that each day is corresponding to a particular set of meditation videos. 

# Usage
Run the program:
```
pipenv run python runmedprogram.py --username [insert gmail] --app_password $APP_PASSWORD --recipients [insert gmail]
```