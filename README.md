## Scripts
This is a script for booking Award Flight on Cathay Pacific. There are currently two scripts. Script_v1.py requires capturing the api url manually and I am currently working on Script_v2.py which will be more automated. It is currently in development.

## Setup

1. Clone this repository
2. Navigate to the folder locally
3. Create a virtual env `python3.11 -m venv venv`
4. Activate the virtual env - `source venv/bin/activate`
5. Run `make requirements`
6. Run `make develop`
7. Check and see if installation was successful `pip list`

## script_v1.py

1. This script requires manually capturing the API url that briefly shows up in Google Chrome when searching for an Award Flight. Copy/Paste the url into the list on line 22.
2. Navigate to `award-booking-script` folder and run `python script_v1.py`
3. This will start a new Chrome session. You will need to manually click `Sign In`
    - It is helpfuly to have these fields pre-filled.
    - If you need more time to sign in, simply adjusts line 44 and increase the time in seconds
4. After `time.sleep(seconds)`, the browser will automatically opens all links defined in the links list.

## script_v2.py

This script is currently under development. It utilizes Selenium and Google Chrome Driver to automate the process of manually selecting desired Award Travel settings such as To, From, Class and Dates.

