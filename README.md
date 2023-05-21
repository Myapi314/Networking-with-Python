# Overview

<!-- {Important!  Do not say in this section that this is college assignment.  Talk about what you are trying to accomplish as a software engineer to further your learning.} -->
This software was built to demonstrate skills in using networking concepts in python. This is a client-server application which incorporates the widely popular Spotify API and a tkinter GUI.

<!-- {Provide a description the networking program that you wrote. Describe how to use your software.  If you did Client/Server, then you will need to describe how to start both.} -->

This client-server application is able to complete several different tasks demonstrating the different capabilities a client-server networking program can achieve. There are several ways this software can be run, but the simplest would be to run both the server and client in individual terminals simultaneously. When the client file is run it will open a tkinter GUI with some options. 

The messaging option has a text entry box from which the user can enter a message and send it to the server. The server receives this message and echoes it back to the client. The log of this is displayed beneath the send message line.

The search for artist option enables the client to enter in the name of an artist and when sent will open a new window with the first ten artists that the spotify API returns. Each is now a button that can be clicked to access two other requests to the server. The user can then request to see their selected artists top tracks or search for their first 20 albums. 

<!-- {Describe your purpose for writing this software.} -->
The goal in writing this is to improve skills in writing requests and understanding client-server applications. The current version can be consistently expanded upon to gain more insight to error handling, and efficiency with writing code in this way.

<!-- {Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running (you will need to show two pieces of software running and communicating with each other) and a walkthrough of the code.} -->

[Software Demo Video](https://youtu.be/jsJdsbIMT4k)

# Network Communication

<!-- {Describe the architecture that you used (client/server or peer-to-peer)} -->

<!-- {Identify if you are using TCP or UDP and what port numbers are used.} -->

<!-- {Identify the format of messages being sent between the client and server or the messages sent between two peers.} -->

This software uses client/server network architecture, communicating via strings or longer strings that the client can parse through. These run using port 5000 and using TCP. 

# Development Environment

<!-- {Describe the tools that you used to develop the software} -->

<!-- {Describe the programming language that you used and any libraries.} -->
To develop this software I used python along with the built in libraries tkinter and socket. I also utilized a library called customtkinter which can be installed running the command ```pip install customtkinter ```. The link to the documentation can be found below. I also utilized the spotify api and created an app using my personal spotify account. To interface with the spotify API I used several built-in modules: os, base64, json, and requests. I also used dotenv to store my environment variables for the authentication into the spotify API. Those who want to run this software locally will have to consult the Spotify documentation for how to get their own client id and client secret, and place them in a .env file with the appropriate variable names. 

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
* Error Handling

    Currently, there is no error handling for the response data and that would be very problematic with practical use of the software. If there is an error on the server side, the client does not handle it very well which is troublesome when processing several different requests such as this software.
* Improved Interface

    As always, there can be improvements made to the user interface of an application. Specifically, I would make the navigation across the different processes more intuitive. I was unable to get the clear response button to be a more regular function that when a user requested a different type of data it would automatically clear the previous response from the screen.
* How data is sent

    With the current version of the software the responses are sent as long strings separated by ?. This honestly isn't as clean as I would want and would probably want it more structured like json data. 