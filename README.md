# ML Model deployement using Flask, postman and docker

Step1: Create the model file

Step 2: Create the main application file(that uses simple python functions and decorators)
a decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it

Step 3: Run the main python file created above which call model predict function to give result at runtime from the main URL link
http://127.0.0.1:5000/predict?variance=25&skewness=20&curtosis=2&entropy=0

Step 4: Test the set up by installing POSTMAN tool to pass test file as Input and see model prediction
POSTMAN can be downloaded from : https://www.postman.com/downloads/

Step 5: Install Flasgger (for creating HTML look and feel for model input)

base) MacBook-Pro-106:Docker_ML_Flask_App atul595525$ pip install flasgger
Collecting flasgger
  Downloading flasgger-0.9.5-py2.py3-none-any.whl (3.8 MB)
     |████████████████████████████████| 3.8 MB 2.0 MB/s 
Requirement already satisfied: jsonschema>=3.0.1 in /Users/atul595525/anaconda3/lib/python3.7/site-packages (from flasgger) (3.2.0)
Requirement already satisfied: mistune in /Users/atul595525/anaconda3/lib/python3.7/site-


Step 6: Create a new main file with Flasgger/Swagger code implemented

Step 7: Run the Flasgger file created above

http://127.0.0.1:5000/apidocs/


Step 8:  Test the result for TestFile

