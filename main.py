from flask import Flask, jsonify, request
from app.controllers.controll import BaseController

app = Flask(__name__)
controller = BaseController('northwind.db')

# Routes for customers
@app.route('/customers', methods=['GET'])
def get_customers():
    customers = controller.select('Customers')
    return jsonify(customers)

@app.route('/customers', methods=['POST'])
def add_customer():
    new_customer = request.json
    controller.insert('Customers', **new_customer)
    return jsonify({'message': 'New customer added'}), 201

@app.route('/customers/<customer_id>', methods=['PUT'])
def update_customer(customer_id):
    updated_customer = request.json
    controller.update('Customers', f"CustomerID = '{customer_id}'", **updated_customer)
    return jsonify({'message': 'Customer updated'})

@app.route('/customers/<customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    controller.delete('Customers', f"CustomerID = '{customer_id}'")
    return jsonify({'message': 'Customer deleted'})

# Routes for other entities can be similarly implemented

if __name__ == '__main__':
    app.run(debug=True)
