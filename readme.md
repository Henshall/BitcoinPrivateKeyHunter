#INFORMATION
This script will guess bitcoin public and private keys and
references them with a list of addresses which have large amount of bitcoin in them.

It is hunting for treasure :)

If the program finds a matching paid it will send you an email.


##SETUP

1) rename the env.example file to env.py (it contains a list of variables which will be used to send you an email)

2) change the variables to suit your needs. This application uses AWS SES CREDENTIALS, So you will need to already have an amazon ses account to use it. You can also simply change the way the emailer works,
which may be easier then signing up for the amazon emailer service

3) run the program with python3 bitcoin_finder.py OR set up a cron job to hit it every minute. It currently examines 9 million keys looking for matches which should take much less then a minute.

Make sure you set the KEYS_FOUND_TEXT_FILE_NAME variable to the full file name of the keys file.

4) Run the following command: chmod -R 777 keys-found.txt    
This will make sure your keys-found.txt file is writable.
You may even want to run a cron job to constantly change this if you are pulling a later version from github


Enjoy!
