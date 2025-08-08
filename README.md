# Internship-Day---4
Build a REST API with flask


First we import flask,request and jsonify. flask is used for creating a web app. request lets us access incoming data and jsonify fromats your response as JSON.
Then we create a flask web application by the name of app= flask().it allos us to initialize the app.
Then we create a dictionary and use a counter to assign id's to new user.
We then use the GET function to return the list of users.POST is used to create a new user,PUT is used to update a user in the 'users' dictionary and DELETE is used to remove or delete a user from the dictionary using pop().
@app is a decorator that tells flask that when someone goes to the route() with any method(GET,POST,PUT,DELETE) give response according to the conditions met.
"debug=True" is used to provide us helpful error messages during development.
