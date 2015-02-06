# Electronic Vote

This project is a python proof of concept for the idea of Electronic Vote. This is just a simple materialization of the 
main ideas that are behind the concept. The purpose of this is mainly academic as we try not to build a full fledged 
working system but instead show that the cryptographic *mambo jumbo* is in reality a fun task and with very interesting
 applications. 
 
 
## Why Python

Well since this is a hacker project no better language than an hacker language. We needed a language with good support
regarding cryptographic operations as well simple to deploy code in a fast way. Python is also an elegant language and
in my own opinion very simple to read. This last point is a important one because since this is a project with academic
purposes it would be nice to work with a language that don't get in the way.


### Third parties

To successfully run this project you must install in your running environment a set of packages needed as dependencies

*   **M2Crypto**
    *   This is a OpenSSL wrapper that is used to run the cryptographic routines needed
*   **SQLAlchemy**
    *   THis is a ORM for operation between the application and databases
    


###Running the tools

To run the service and tools you must first set the python path in your shell. If you're using linux you can do that
by writing 

        export PYTHONPATH=$(pwd)
        
inside the **evote/evote** folder

To run the web application you can do 

        python web/service.py
        
To create a public/private pair of keys you can execute

        python tools/evote.py  -g kpair -l 2048 -o user

This will create in the current folder the files **user_priv.der** and **user_pub.pem** that are the public and
private key respectively
        
After the service is running and you got the keys you can create users in the platform by invoking, for example, 
the command

        python tools/evote.py -g user -n user -Pk user_pub.pem -m user@user.net


To check all this working open the **evote/evote/database/evote.db** SQLite database and check for the user 
 table. If everything is ok you'll see a new user with a public key, like in the following image
 
 ![EVote User](http://shared.balhau.net/evote/newuser.png "EVote new user")

###Notes

For this project we use the **PyCharm IDE** (open edition) that is very recommended. It integrates very well with unit
testing and is very nice to work. You should give it a try. 
