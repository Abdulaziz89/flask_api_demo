from flask import Flask, jsonify, request
import json
import sqlite3

application = Flask(__name__)

with open('data.txt') as json_file:
    companies = json.load(json_file)


@application.route('/', methods=['GET'])
def home():
    return '<h1> API demo </h1>'


# return all of the companies
@application.route('/api/v1/resources/companies/', methods=['GET'])
def get_all():
    return jsonify(companies)


# return info for a specific companies
@application.route('/api/v1/resources/companies/<name>', methods=['GET'])
def get_company(name):
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


# returns items as dictionaries {col: row}
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


# return all of the companies, from a DB
@application.route('/api/v2/resources/companies/<name>', methods=['GET'])
def get_all_db(name):
    with sqlite3.connect('database.db') as conn:
        conn.row_factory = dict_factory
        cur = conn.cursor()
        all_companies = cur.execute("SELECT * FROM Companies WHERE name=?;", [name]).fetchall()

        return jsonify(all_companies)


# run the app.
if __name__ == "__main__":
    application.debug = True
    application.run()
