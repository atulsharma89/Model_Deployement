# ML Model deployement using Flask, postman and docker

Step1: Create the model file

Step 2: Create the main application file(that uses simple python functions and decorators)
a decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it

Step 3: Run the main python file created above which call model predict function to give result at runtime from the main URL link
http://127.0.0.1:5000/predict?variance=25&skewness=20&curtosis=2&entropy=0

Step 4: Test the set up by installing POSTMAN tool to pass test file as Input and see model prediction
POSTMAN can be downloaded from : https://www.postman.com/downloads/
