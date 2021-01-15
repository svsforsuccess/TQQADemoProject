# TQQADemoProject

Following test cases are covered as part of demo project 

1.Create New User using SuperUser with dynamically created username and password -->validate in dashboard ,whether new user created with dynamically created email and user details by travelling to the last page of the dashboard using enable capability of page navigation .

2.Change password after logging in and validate new password is working by logging in with new password.

How to execute test cases?
Create new project folder 

git clone https://github.com/svsforsuccess/TQQADemoProject.git

And open the terminal in the path and execute following commands

cd testcases
pytest Test_CreateUser.py --alluredir /Reports


Open the reports in the following path using following command

allure serve \Reports








