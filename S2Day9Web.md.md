# What is Web Application
- It is a program that runs on a web server to perform specific tasks.
- Websites consists of 
	- Front End (client Side)
		- It is the page which we access
		- The programming languages and Frameworks to build front end of a website are:
			- HTML, CSS, JS(react)
		- Front end developer.
	 - Back End(server Side)
		 - users don't have interaction with it but their request will be sent to the server
		 - The languages are:
			 - JS (node.js), Python (Django, Flask), PHP, SQL
		- Back end developer
- And a person who develops both "Full Stack Developer"
# HTML (Hyper Text Markup Language)
- A mark up language refers to a text encoding system consisting of symbols inserted in a text document to control its structure, formatting, or the relationship between its parts.
- It tells the browser how to display the content.
- It have tags (special words that have <>on their beginning and ending) :
	- <>  <> - The text between these tags are called "inner text".
	- <>  <>  <>  <>  tags inside tags are called "inner HTML"
- Every code doesn't have closing tag
	- <(img)>b
### Simple HTML docments
- Got two contents :
	- Head tag
		- It contains elements which does not appear on the page
	- Body tag
		- It contains all visible contents
There are heading tags:
```html
<h1>   <h1>
<h2>   <h2>
<h3>   <h3>
```
# Web browsers
- They are used to read html file (it does not display the html tags).
```HTML
<html>
	<head>
		<title> HACHALU KETEMA </title>
	</head>
	<body>
		<h1>Introduction</h1>
		<p>MY name is hachalu ketema, and currently i am learning hackng and this is the first html file i have ever written .
		<a herf="https://google.com"> check here </a>
	</body>
</html>

```
# What is web hacking
- It refers to exploiting of applications via http which can be done by manipulating the app via its graphical web interface.
## How do websites work?
- When you click a link, it will send HTTP request to the server and get the copy of the website to the client this is called HTTP Response.
### URL and URI
- URI identifies: a resources and differentiates it from others by using a name, location, or both.
	- This aims to identify a resource and differentiate it from other resources b using the name or location of the resource. 
- URL identifies: the web address or location of a unique resource.
	- It aims to find the location or address of a resource.
#### Parts of URL
- It contains 5 parts :
	1. Scheme: Tells web server which protocol to use when it accesses a page on your website 
	2. Subdomain: It means specific part of the website.
	3. Top-level domain: It will specific what type of entity your organization registers as on the internet.
	4. Second-level domain: Is the name of the website 
	5. Subdirectory (subfolder): Helps to understand which type of web is it. 
![[Pasted image 20230826215530.png]]

- For apache server examples :
	- /var/www/html/technology/fields
## HTTP request and response
- They are a request which the browser sends to the server
- And the responses come from the server to the browser
- This are sent and receved with a header.
### HTTP Header
- Used to pass information between the clients and servers.
- The end of header section denoted by an empty header.
#### Types of Header
1. General Header: It is applied on Request and Response
2. Request Header: Contains info about the request.
3. Response Header: Contains the location of the source that has request 
4. Entity Header: Contains info about the body of the resource like content length. 
##### Request Headers
The 1st line Contains
● Request Method
● Path: The path where the file/folder is located
● Protocol Type: which HTTP protocol ( HTTP 1 , HTTP/1.1 , HTTP/2
The 2nd line
● Host: the website link
The 3rd line
● Cookie: used to check a user
The 4th line
● User-Agent: used to place the browser information![[Pasted image 20230827091041.png]]
##### Response Header
 This is response from The server to the browser
● 1st line
○ HTTP: Tells the server Protocol 
○ Status Code
● 2nd line
○ Date: Date of the response sent
● 3rd line
○ Content-Type: What type of content the server sent 
Encode type
● 4th line
○ Content-length: The number of the alphanumeric and 
spaces
● 5th line
○ Server: type of the webserver
● 6th line
○ This line is empty used to show that the headers 
ending. And beginning of the body
● 7th…. Line
○ The html content

## HTTP request methods
● The method designates the type of request being made to the web server. 
● The most common types of request methods are GET and POST but there are many others, 
including HEAD, PUT, DELETE, CONNECT, and OPTIONS.
## HTTP Status Code
● The Status-Code element in a server response
● is a 3-digit integer where the first digit of the Status-Code defines the class of 
response and the last two digits do not have any categorization role. 
● There are 5 values for the first digit:
○ 1xx: Informational
■ It means the request has been received and the process is continuing.
○ 2xx: Success
■ It means the action was successfully received, understood, and accepted.
○ 3xx: Redirection
■ It means further action must be taken in order to complete the request.
○ 4xx: Client Error
■ It means the request contains incorrect syntax or cannot be fulfilled.
○ 5xx: Server Error
■ It means the server failed to fulfill an apparently valid request.
## Some common codes
● 200 = request is Successful( OK )
● 301 = The requested page has moved to a new url . ( Moved Permanently ) 
● 302 = The requested page has moved temporarily to a new url .( Found ) => when there is redirection
● 400 = The server did not understand the request. (Bad Request)
● 401 = The requested page needs a username and a password. (Unauthorized)
● 403 = Access is forbidden to the requested page.(Forbidden)
● 404 = The server can not find the requested page.(Not Found)
● 405 = The method specified in the request is not allowed.(Method Not Allowed)
● 500 = The request was not completed. The server met an unexpected condition.(Internal Server Error)
_____
THE HEADERS ARE SHOWN ON :
	Developers tool (on browser)
	curl
	burp suite
# Developers Tool
- Can be opened by ctrl + shift + c
- Consists :
	- Inspector: to see and edit the HTML and CSS temporally
	- Console: to run some Java script codes
	-  Debugger: used to do debug in runtime 
	-  Network: to see the requests and responses
	-  Storage: to store catch and cookies
	- To get the requests we go to the Network tab
# Curl on Linux
- Curl stands for client URL - it is a tool that is used to transfer data to and from server.
- It supports different protocols like HTTP and HTTPS .
# Burp Suite
- Used for penetration testing of web application.
- Developed by Portswigger.
- Is an integrated platform and graphical tool for performing security testing of web applications.
- Helps to act like a proxy. 
___
After the installation and  activation steps :
### Opening Burp
- Burp helps to 
	- open project
	- Create a new project
	- Use temporary project
### Starting Burp
- There are tabs used for many purposes, this are:
	- Target: to add target and see progress
	- Proxy: to setup proxy IP and to interrupt and watch request and response. 
	- Intruder: to do brute force 
	- Comparer: to compare 2 requests and responses. 
- To connect burp with browser.
	- To do this we have to install proxy plugin
		- foxy proxy
	- Then we need to add the burp proxy .

# OWASP Top 10
- It stands for Open Web Application Security Project.
- This project releases top 10 vulnerability  every 4 year and also API vulnerability .
- https://owasp.org/Top10/
## Brute Force
- It is included in Broken Authentication/ Access Control Bug
- It is usually used to done login pages
- It uses a word list to check the username and password.
## XSS
- Included in injection BUG
- This Bug is exploited. As the following
	- If there is a search place and the search place expects a text to search and displays below.
	- But if we add some html/JS codes on that place, this means it will add the code to the inner HTML
	-  SO our code will be executed!

 ## SQL injection
 - It is included in the Injection Bug
 - Same with xss but in this one we will add a sql code to the search place.
 - It is query language used in back end to retrieve data from database.
 - Used to bypass login pages
 ## Rate Limit
 - Is is a limiting problem which will limit the request the will be sent from  a client .
 ## Access Control
 - This problem occurs on how a website control an access of a user, if there is a problem in the access control normal user can get an admin access.
 ## IDOR
 - Stands for Insecure Direct Object References and it is a bug included on access control.
 - This will happen when you have id number 1
 ## Business Logic
- This bug is logic flow.

[[S2Day10Wireless.md]]
