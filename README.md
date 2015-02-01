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

###Notes

For this project we use the **PyCharm IDE** (open edition) that is very recommended. It integrates very well with unit
testing and is very nice to work. You should give it a try. 