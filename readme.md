# Bitcoin Private Key Hunter

This package can help you hunt for bitcoins. It works by randomly generating a bitcoin private key, finding the corresponding public key / bitcoin address, and checking this key against a list addresses known to hold a lot of bitcoin. If a match is found, it will save the private key, public key, and other types of key formats generated into a text document and email you with the information as well.

## Setup:
- Download the package
- Make sure python3 and all of the projects dependancies are installed
- update the env.example.py file with your amazon SES information
- copy the env.example.py file into a file called env.py
- run th example file given to start. See below for code.
```bash
git clone https://github.com/Henshall/BitcoinPrivateKeyHunter.git
cp env.example.py env.py
python3 example.py
```

## Usage:
The Bitcoin Finder uses a number of other classes to perform its function. However its main function is to pull everything together so that you can effectively send yourself an email and save any keys you find. You can hunt for bitcoins with the following:
```python
finder = BitcoinFinder()
finder.setEnv(env)
finder.setAddressList(["pk1", "pk2"])
finder.start()
```

You will want to set an env file (to hold your SES info), if you fail to set the env file, you will not receive an email, but you can still use the application. The application will fail however if you fail to set an AddressList - a simple array of private keys.


Enjoy!

