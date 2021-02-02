from flask import Flask, jsonify, request
import json

application = Flask(__name__)

with open('data.txt') as json_file:
    companies = json.load(json_file)


@application.route('/', methods=['GET'])
def home():
    return '<h1> API demo </h1>'


# return all of the companies
@application.route('/api/v1/resources/companies/', methods=['GET'])
def api_all():
    return jsonify(companies)


# return info for a specific companies
@application.route('/api/v1/resources/companies/<name>', methods=['GET'])
def api_id(name):
    results = []

    for company in companies:
        if company['name'] == name:
            results.append(company)
    return jsonify(results)


# add a new company to the list
@application.route('/api/v1/resources/companies', methods=['POST'])
def add_company():
    company = {
        'id': companies[-1]['id'] + 1,
        'name': request.json['name'],
        'revenue': request.json['revenue'],
        'employees': request.json['employees'],
    }
    companies.append(company)
    with open('data.txt', 'w') as file:
        json.dump(companies, file)
    return jsonify({'company': company}), 201


# remove an existing company from the list
@application.route('/api/v1/resources/companies/<name>', methods=['DELETE'])
def remove_company(name):

    for company in companies:
        if company['name'] == name:
            companies.remove(company)
    with open('data.txt', 'w') as file:
        json.dump(companies, file)
    return 'removed ' + name + ' company'


# run the app.
if __name__ == "__main__":
    application.debug = True
    application.run()
