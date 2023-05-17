# Overview

<!-- {Important!  Do not say in this section that this is college assignment.  Talk about what you are trying to accomplish as a software engineer to further your learning.} -->
This software was built to demonstrate skills in using networking concepts in python. This is a client-server application which incorporates the widely popular Spotify API and a tkinter GUI.

<!-- {Provide a description the networking program that you wrote. Describe how to use your software.  If you did Client/Server, then you will need to describe how to start both.} -->

This client-server application is able to complete several different tasks demonstrating the different capabilities a client-server networking program can achieve. There are several ways this software can be run, but the simplest would be to run both the server and client in individual terminals simultaneously. When the client file is run it will open a tkinter GUI with several options. 

{INSERT IMAGE}

{INSERT EXPLANATION OF EACH OPTION}
The messaging option has a text entry box from which the user can enter a message and send it to the server. The server receives this message and echoes it back to the client. The log of this is displayed beneath the send message line.

The search for artist option enables the client to enter in the name of an artist and when sent will open a new window with the first ten artists that the spotify API returns.

<!-- {Describe your purpose for writing this software.} -->

<!-- {Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running (you will need to show two pieces of software running and communicating with each other) and a walkthrough of the code.} -->

[Software Demo Video](http://youtube.link.goes.here)

# Network Communication

<!-- {Describe the architecture that you used (client/server or peer-to-peer)} -->

<!-- {Identify if you are using TCP or UDP and what port numbers are used.} -->

<!-- {Identify the format of messages being sent between the client and server or the messages sent between two peers.} -->

This software uses client/server network architecture. These run using port 5000

# Development Environment

<!-- {Describe the tools that you used to develop the software} -->

<!-- {Describe the programming language that you used and any libraries.} -->
To develop this software I used python along with the built in libraries tkinter and socket. I also utilized a library called customtkinter which can be installed running the command ```pip install customtkinter ```. The link to the documentation can be found below. I also utilized the spotify api and created an app using my personal spotify account. To interface with the spotify API I used several built-in modules: os, base64, json, and requests. I also used dotenv to store my environment variables for the authentication into the spotify API. Those who want to run this software locally will have to consult the Spotify documentation for how to get their own client id and client secret.

# Useful Websites

<!-- {Make a list of websites that you found helpful in this project} -->

<!-- Used for initial client/server setup -->
* [Digital Ocean - Python Socket Programming](https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client) 
* [Spotify for Developers](https://developer.spotify.com/documentation/web-api)
* [How To Use Spotify's API with Python](https://www.youtube.com/watch?v=WAmEZBEeNmg)
* [Geeks for Geeks - tkinter](https://www.geeksforgeeks.org/python-gui-tkinter/)
* [Custom Tkinter Intro](https://medium.com/@fareedkhandev/modern-gui-using-tkinter-12da0b983e22)
* [CustomTkinter Documentation](https://customtkinter.tomschimansky.com/documentation/)

# Future Work

<!-- {Make a list of things that you need to fix, improve, and add in the future.} -->
* Item 1
* Item 2
* Item 3