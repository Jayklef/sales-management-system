APIs and RESTFULNESS

What is API

The acronym API means Application Programming Interface and it is the gateway to backend data. An API allows different services to communicate with each other, exchange information and also makes it possible for a service to access the functionalities of other services. APIs are like a Bank Teller whom bank customers go to to perform several activities (deposit, withdrawal, check balance etc) in their account. The bank teller acts as an intermediary between the bank customer and the customer account.

RESTful APIs




REST stands for Representational State Transfer, it is an architectural style for designing APIs. It essentially highlights certain guidelines to be adhered to when designing APIs that allows for loose coupling and scalability by using Hypertext Transfer Protocol (HTTP) methods when building APIs that facilitates interaction between client-side and server-side applications. Restful APIs provide an easy way to communicate with a server.  An API is therefore considered a Restful API if it conforms to the representational state transfer (REST) architectural style. Developers can design Restful APIs in any programming language but the must conform to the six (6) REST design principles also known as design constraints below:

Client-Server Architecture
There should be a server that is serving the information and a client consuming the information and they must be independent of each other. The client can only interact with the server via the URI and the server shouldn’t be able to modify the client information

Cacheable
It should be possible for responses to be saved by a web browser, server or any system. This can help reduce server load by using the API result from the cache instead of making request to the server every time. Server resource should also contain information regarding whether caching is allowed for the delivered resource 

Layered Architecture
This means that the entire system can be split into multiple layers and REST APIs should be designed in a way that neither the client nor the server can tell tether it is communicating with the end application or an intermediary. The layers of a Resfl API could include a load balance, a web server and a database

Stateless



Uniform Interface
Code on Demand




What are restful APIs
Explain RESTfulness
HTTP vs HTTPs - Encryption and decryption are performed at both the client and server side
HTTP Methods, status codes and response types
Connecting the Dots: REST and CRUD
Naming conventions
Good and Bad Routes
API Naming conventions
Tools for API development
Best Practices for Building APIs
Caching
Rate Limiting
Monitoring
Versioning
Keeping it simple

Authentication and Authorization


Security and Authentication in REST APIs - APIs give 3rd party apps access to your server and backend services and hence it is necessary to properly secure them



Status Codes
100 - 199 - Informational
200 - 299 - Successful
300 - 399 - Redirection
400 - 499 - Client error
500 - 599 - Server error




Authentication versus authorization
Introduction
You need to secure your APIs because they provide third-party clients access to your backend data. If you don’t secure your APIs properly, anyone can tamper with the data and access sensitive information. But even if a client is allowed to access the data, you need to control who can do what. This is where authentication and authorization come in. You now know that although they sound similar, they are not the same. In this reading, you will learn about the difference between authentication and authorization and how you can use it to protect your API endpoints.
Authentication
Authentication is the process of verifying the credentials of a user. Logging into websites with a username and password is a typical example of authentication. When the username and password match, the website recognizes the user and sets some cookies in the user’s browser. When the user visits another page on that website, the browser sends those cookies within the HTTP request header. The website recognizes the cookies as well as server-side session data and therefore doesn’t ask for credentials until the user logs out again. 
So, how does this work? Token-based authentication usually involves two steps in the API Architecture. First, the client identifies itself with a username and password. Then the API server gives it a bearer token. From there, the client includes the bearer token with every API call that it places. The API server verifies it and then allows the client to perform the action or not. This is where authorization comes in, but more on this later.
If the credentials are not valid, the client will receive a 401 - Unauthorized HTTP status code.
This is like coming to the office on the first day, submitting all your papers and documents, and then receiving your employee card. After that, only your employee card will be sufficient to get inside. Authentication works just like that!
The two steps in the API authentication process can be represented by the following two diagrams.
Authentication process: Getting an access token

Authenticated API calls

     
Authorization
However, even with your employee card, you will not be able to access all the rooms or spaces in the office. There are some places that are only accessible to a certain group of people who have been given that privilege. Authorization is exactly like that. Authentication lets you in, authorization lets you act. It checks after authentication if the user has the proper privileges to perform some tasks.
On the server side, this is typically done by assigning the user to a group or a set of groups. Then, after verifying the token, the code checks if the user belongs to the appropriate group to perform that task. If not, the client will receive a 403 - Forbidden HTTP status code.  
API authorization

This extra authorization layer in the API architecture ensures that only people with proper privileges can access and modify data. An authorization system in an API project is very important because it prevents data corruption and data breaches.
Implementing authorization
Privileges are the tasks that an API user performs, and they are the building blocks of an authorization layer. First, as an API developer, you identify the required privileges in your project. For example, for a bookshop, there might be the following types of privileges:
Browse the books
Add new books
Edit books
Delete books
Place orders
There can be many other privileges like this. And not every user will have every privilege. For instance, regular customers are not allowed to add and edit books, even if they are properly authenticated. Only managers are allowed to perform those operations.
So, after identifying the privileges, you carefully distribute all these privileges into multiple roles. And then, the authorization check is done in the backend code of each API endpoint that requires a user role check. The developer verifies if the user belongs to the appropriate group or roles, and then makes the decision to allow or deny the action.
User groups in Django
The Django admin panel comes with excellent support for the user group system. If you log into the admin panel, you will find two distinct sections – users and groups.

From here, you can create groups or roles like Manager, Editor, Customer, Admin and so on and assign privileges to these groups. If you click on the Add button next to the groups, you will be taken to a screen where you can create new groups. The Django admin panel will list all the necessary privileges based on the models in your project. Here is a screen that indicates the available privileges for a bookshop.    

   
On this screen, you can create an Editor role, for instance, and add privileges to it.

   Or you can create a Customer role that will have different privileges.

The Django admin panel allows you to manage groups throughout the project. You can add and remove privileges to groups as the project grows.

But creating groups with privileges is not enough. After creating these groups and assigning users to them, you need to write some code in the function or class-based views that determine if authenticated users belong to those groups and then make decisions based on that. But you will learn to do this later in the course.
Conclusion
Authentication and authorization are concepts that differ in function and how they are set up in an API architecture. The knowledge you gained in this reading about user groups, roles and privileges lay the groundwork for all the steps that you will learn later on for setting up a proper security layer in your API projects.


Consequences of a poorly designed API project
Introduction
Creating a good API project can be challenging. You need to stick to the conventions, write proper error checks in your code, perform security checks, and make sure that your APIs are using processing power and bandwidth optimally. This all takes time and proper planning. But what happens if you don’t properly plan and execute your APIs?
Let’s examine some of the consequences of a poorly designed API project.
Data breach  
Reasons
Consequences
Poor security checks in the code, no authentication or authorization checks, improper file permission, and not using SSL
The most significant risk of a poorly designed API project is a data breach. Sensitive data can leak if you don’t have proper security checks in your code or if you didn’t implement proper permissions for the files stored on the server.
Also, if you are not using SSL for your API endpoints, attackers can steal user data before it reaches your API web server.
Such mistakes can cause severe financial damage and trust issues.

Fix: Add proper security checks in your code and create a solid authorization layer to prevent unauthorized access to your data. Always double-check these sensitive API endpoints before deploying them to production.  
Data corruption
Reasons
Consequences
Poor security, no authentication or authorization checks, absence of data validation and sanitization of input data
Improper security checks and lack of a solid authorization layer can let any user with a valid authentication token access sensitive APIs and modify the data unexpectedly. Also, creating resources without proper validation checks can create malformed data in the database.
Such mistakes can cause severe data corruption and data loss beyond repair.

Fix: Besides security checks and a solid authorization layer, an API developer must validate and sanitize user data before processing and saving it.
Wastage of computing power and memory
Reasons
Consequences
Unoptimized code, improper business logic, lack of data validation, unoptimized SQL queries or model relationships, lack of database indexes, and no caching.
Poorly written API code can consume unnecessary computing power and memory with unoptimized code, algorithms and business logic. Unoptimized code, lack of proper database indexing and absence of caching can cause a huge load on the database server by running redundant SQL queries, which slows the whole system down.
Such mistakes can end up increasing the cost of your API infrastructure.

Fix: To avoid this, always spend time optimizing the code and double-checking your database-related code before deploying your APIs to production.
Wastage of bandwidth
Reasons
Consequences
Absence of necessary caching header API code, lack of caching policy on the reverse proxy and on the web server, and lack of pagination and filtering.
If your API project doesn’t follow good API development practices like implementing caching, filtering and pagination can cause your APIs to deliver unnecessary data more times than what is required.
Such mistakes can cause bandwidth wasting and end up charging extra bills in your monthly invoice, as well as poor performance from your API endpoints. Besides, the client applications need to spend more resources and time filtering unnecessary data every time.

Fix: To avoid this, always send proper caching headers with your API responses and implement filtering and pagination features so that the client application can request and receive only what they need.
Bad user experience
Reasons
Consequences
Not following the proper naming convention, not sending proper HTTP codes, not accepting Accept headers, absence of pagination, sorting, searching and filtering, and lack of proper error checking in code.
It creates a bad user experience. The client application developers must go through extra processing of the API data, extra code to create the final output, and a steeper learning curve to use your API, which was not necessary if the API was designed by following the standard conventions and best practices.
Not accepting the Accept headers means that the API client is not getting the API output in its required format. That will cause bad experiences because clients need extra time and unnecessary code to process the data on their end.   
Also, sending wrong HTTP status codes can cause unexpected errors on the client applications and a bad experience for the users who will use those applications.

Fix: To avoid this, always follow the proper naming convention and implement data filtering, searching, sorting, searching and pagination features for your API endpoints. Always keep proper error checking in the code and write tests so that it doesn’t create unexpected 5XX errors on the server side.
Breaking client applications
Reasons
Consequences
Not following the proper versioning system
If you don't maintain the proper versioning system for your API project, it can immediately break backward compatibility, and the client application can stop working instantaneously.
The API can cause failure in the current client applications because your new API requires new request data and delivers new responses. So, their old code will not work anymore. They must refactor it and release a new version of their application as soon as possible.
Such disruption can cause a bad reputation and financial damage for both the API and client application developers.

Failure to manage the app
Reasons
Consequences
Keeping everything in one big Django app, adding all business logic in the views.
Django apps can become big and become unmanageable over time if you keep adding functionalities in one single app. And then, adding new features or debugging an error will be painful and take extra time and effort.
Also, adding all business logic in the views file can lead to writing redundant code across multiple classes and function-based views.
Failure to manage an app over time leads to bad coding, patching of errors without test coverage and ultimately, poor performance from the APIs. 

Fix: Distribute the features and functionalities to multiple smaller Django apps in a decoupled way. Additionally, put some business logic in the models which can be reused by the other parts of your API project.
Conclusion
Taking the time to properly design an API project from the start will save you time and effort over the course of a project. The consequences of a poorly designed API affect everyone who uses your API, including the API developers and client application developers.
The knowledge you gained in this reading will hopefully remind you of everything you need to keep in mind to make your future API projects successful.

