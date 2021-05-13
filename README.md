## Vityasa Internship Task

## API Documentation

## Bonus Steps followed:

- Bonus 0: Solved all the questions
- Bonus 1: Used coding best practices such as linting, naming conventions, documentation etc.
- Bonus 2: Used a popular Python web framework (Django)

## Steps to start the project:
- Open the folder Question 1 or Question 2 or Question 3
- In this folder, run manage.py runserver
- Now, any request can be sent according to the question
- Requests can be sent using POSTMAN or any other similar application
- The code for the app can be found in Answer1, Answer2 and Answer3 folders in the respective Question directory


## Given below are the api endpoints for each question

## Question 1:
## items (POST): api endpoint to find details of valid positive integers and number of values that are invalid
- Usage: http://127.0.0.1:8000/items/?data=1&data=4&data=-1&data="hello"&data="world"&data=0&data=10&data=7
- Return type: Json
## Question 2:
## booking/ (POST): api endpoint to create a booking
- Usage: 
http://127.0.0.1:8000/booking/
Body: 
{
  "slot": 1, "name": "John"
}
- Return Type: Json
## booking/ (GET): api endpoint to view all bookings
-  Usage: http://127.0.0.1:8000/booking/
- Return Type: Json
## cancel/ (POST): api endpoint to cancel a booking
- Usage: http://127.0.0.1:8000/cancel/
Body:
{
  "slot": 1, "name": "John"
}
- Return Type: Json
## Question 3:
## plot/ (POST): api endpoint for finding out if points given form a square or not
- Usage: http://127.0.0.1:8000/plot/
Body:
{
  "x": 1, "y": 1
}
- Return Type: Json
