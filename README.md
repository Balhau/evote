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

To list the surveys that are already created you can do

	python tools/evote.py -L survey
	


This will output a json string with all the surveys present in the database, for example:

	[{"description": "Elei\u00e7\u00e3o para presidente do benfica do ano de 2014/2015", "id": 1, "name": "Presidente do Benfica 2014/2015"}]



This will create in the current folder the files **user_priv.der** and **user_pub.pem** that are the public and
private key respectively
        
After the service is running and you got the keys you can create users in the platform by invoking, for example, 
the command

        python tools/evote.py -g user -n user -Pk user_pub.pem -m user@user.net


To check all this working open the **evote/evote/database/evote.db** SQLite database and check for the user 
 table. If everything is ok you'll see a new user with a public key, like in the following image
 
 ![EVote User](http://shared.balhau.net/evote/newuser.png "EVote new user")


##Organization

This project consists of several little components.

### Web

The web component, which is inside the *evote/web* folder consists of a web application done with the help of the [Flask Framework](http://flask.pocoo.org/), wich is a mvc engine to help deploy easy and with little boilerplate code a web server running by default on **[Localhost:5000](http://localhost:5000)**. The web component is the front end for the operations on the [SQLite](https://sqlite.org/) database that holds all the relevante data. 

### Database
The database component is composed by some *Python* scripts and models inside the *evote/database* and *evote/database/models* folders. Here we have the ORM implementation built uppon the [SQLAlchemy framework](http://www.sqlalchemy.org/).
You must note that with a little tweek you can adapt to use it with a [MySQL](https://www.mysql.com/) or [PostgreSQL](http://www.postgresql.org/) database

### Shell Tools

You can invoke the services available in the web component and in this way do something usefull by invoking the commands that are available in the *evote/tools/evote.py* script. This script allows you do several operations, as described previously, by invoking the **Json RPC** available in the web component.

###Gui

In the future, we hope next future, it will be added a Gtk based GUI to enable people who don't like to play with the shell to use the services available.


##FAQ's

* It is known that public key cryptography is not good to cypher/sign large volume of data. Since you don't use symmetric algorithms isn't this extremely slow?
	* Yes public key cryptography is several orders of magnitude slower than the symmetric algorithms. We solve this problem by not signing large volume of data. We use hash functions before signing the data, and by doing this we avoid the large data problem. This strategy works fine for signing protocols which is the case. Since we don't cypher the data we can afford to use only public key algorithms. If, in the future we need to cypher data we must do it by providing a list of symmetric algorithms and respective keys.

* From the web server part we see that the data is not ciphered through the network, isn't this a problem?
	* Sure it is. But honestly its just a matter to add ssl over the network and in this way the problem is solved. Since by doing it we only would had increase the complexity this *detail* was kept aside. But in future work the http conection will be replaced by a https with certificate validation of the server by the client side

##Notes

For this project we use the **PyCharm IDE** (open edition) that is very recommended. It integrates very well with unit
testing and is very nice to work. You should give it a try. 
