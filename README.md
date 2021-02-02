# Getting Started with Creating REST API using Flask

To get started, you can go through this sample Python Flask app, that will help you set up a development environment, and create a couple of different REST APIs.



## Prerequisites

* [Python](https://www.python.org/downloads/)

## 1. Clone the sample app

Clone the repo and change to the directory where the sample app is located.
  ```
git clone https://github.com/Abdulaziz89/flask_api_demo.git
cd flask_api_demo
  ```


## 2. Run the app locally

Install the dependencies listed in the [requirements.txt](https://pip.readthedocs.io/en/stable/user_guide/#requirements-files) file to be able to run the app locally.

You can optionally use a [virtual environment](https://packaging.python.org/installing/#creating-and-using-virtual-environments)
  ```
pip install -r requirements.txt
  ```
  
Create the SQLite DB.
  ```
python create_db.py
  ```
  
Run the app.
  ```
python application.py
  ```

 View your app at: http://localhost:5000

## 3. Prepare the app for deployment

To deploy your app to AWS Elastic Beanstalk, group the following files in a zip file. 

- requirements.txt
- application.py
- data.txt
- database.db

## 4. Deploy the app

Create a new Amazon Account at https://aws.amazon.com/education/awseducate/.

Go to your AWS Console.

Create a new Elastic Beanstalk, and add a new application, select Python as your platform

Upload your code. 


## 5. Test the app

Get a list of all the companies
  ```
http://[yourdomain.com]/api/v1/resources/companies/
  ```
  
Get info for a specfic company 
  ```
http://[yourdomain.com]/api/v1/resources/companies/apple
  ```

Add a new company 
  ```
run the following command
curl -X POST http://[yourdomain.com]/api/v1/resources/companies -H "Content-type:application/json" -d "{\"name\":\"test\",\"revenue\":\"500\",\"employees\":\"111\"}"
  ```
  
Delete an existing company
  ```
run the following command
curl -X DELETE http://[yourdomain.com]/api/v1/resources/companies/test   ```
