# Password-Checker
This is a Python Scripting Mini Project. This project is aimed at learning the use of website API's and use of hashing. This mini project includes a password validator and then checks for the password related information and displays the relevant data to the user in layman language.

This code uses the following python libraries:
1. Requests - This module allows to communicate with HTTP server using Python
2. Re - This library is used to handle pattern matching through regular expression
3. Hashlib - This library is used to implement various hashing and message digest algorithms
4. sys - This library is used to get user input when executed through command prompt. ( System Input ) 

Functions in the project:
1. fetch_api_data() :- To request api data 
2. check_pwned_api() :- Check if the password exists in API Database
3. get_leak_count() :- Compare the password from database and get the hack count
4. match_password_pattern() :- It checks if the password matches a pattern of characters and allows further processing
5. display_data() :- Display the final result and suugest if the password is safe
