# Mathematician
A repository hosting a mathematics quiz app

# How to use (test if it's working for you)

After cloning the repository go to the repositories main directory AND
open your terminal and use the following command
`pip install -r requirements.txt`<br>
then use <br>
`django manage.py runserver` command to start the server.
Now go to the local host `http://127.0.0.1:8000/` and you will see the home page!
![image](https://user-images.githubusercontent.com/87518251/183300713-a94c4cb8-0871-4bcb-a6d9-b2f0c951de36.png)

Now click on a quiz to start it,

You will see something like this: 
![image](https://user-images.githubusercontent.com/87518251/183300827-e2e6c8e0-56dd-405e-aa20-6d7ebcf8a1b6.png)

Now answer all the questions and submit and you will be able to see the result:
![image](https://user-images.githubusercontent.com/87518251/183300946-115ae60a-9307-42e9-a63a-15484537f879.png)


# Add New Questions and Test

Create a superuser using `python manage.py createsuperuser`

1. First add another card to home page linking to /quiz/quiz name/
2. Go to `127.0.0.1:8000/admin`
3. Login with the credentials of super user
4. Go Tests tab and create a new test with name equals to `QUIZ NAME` used in the link
 ![image](https://user-images.githubusercontent.com/87518251/183301142-563cbd16-59d5-47db-af07-687b7f897e32.png)
5. Congrats you have created a new test

## Add questions 

1. Move to the questions model from sidebar and click on Add question
2. You should see something like this
![image](https://user-images.githubusercontent.com/87518251/183301196-f2cb809a-9665-4bc3-a058-fb1924571a09.png)
3. Type the question in the question text field (You can use html or plain text)
4. Click on `Add Answers` to write choices
5. Mark if a choice is correct or Not
6. In the course field select to whic test question belong (Test Object 1, 2,3,4,....,etc)

Click `SAVE` and you are done!
