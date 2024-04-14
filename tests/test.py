# import requests
# import unittest

# # Base URL of the Flask API
# base_url = 'http://127.0.0.1:5000/'

# class TestAPI(unittest.TestCase):
#     def test_get_customers(self):
#         response = requests.get(f'{base_url}/customers')
#         self.assertEqual(response.status_code, 404)

#     # def test_add_customer(self):
        
#     #     new_customer = {
#     #         "CustomerID": "NEWCUST",
#     #         "CompanyName": "New Company",
#     #         "ContactName": "John Doe",
#     #         "ContactTitle": "CEO",
#     #         "Address": "123 Main St",
#     #         "City": "Anytown",
#     #         "Region": "Region",
#     #         "PostalCode": "12345",
#     #         "Country": "USA",
#     #         "Phone": "555-1234",
#     #         "Fax": "555-5678"
#     #     }

        
#     #     response = requests.post(f'{base_url}/customers', json=new_customer)

#     #     try:
            
#     #         response.raise_for_status()
            
#     #         print(response.json())
#     #     except requests.exceptions.HTTPError as err:
            
#     #         print(f"HTTP Error: {err}")


#     # def test_update_customer(self):
#     #     customer_id = 'NEWCUST'  # Assuming the ID of the customer to be updated
#     #     updated_customer_data = {
#     #         "CompanyName": "Updated Company",
#     #         "ContactName": "Jane Doe",
#     #         "ContactTitle": "CTO",
#     #         "Address": "456 Elm St",
#     #         "City": "Othertown",
#     #         "Region": "Region",
#     #         "PostalCode": "54321",
#     #         "Country": "Canada",
#     #         "Phone": "555-9876",
#     #         "Fax": "555-4321"
#     #     }

#     #     response = requests.put(f'{base_url}/customers/{customer_id}', json=updated_customer_data)

#     #     try:
#     #         response.raise_for_status()
#     #         print(response.json())
#     #     except requests.exceptions.HTTPError as err:
#     #         print(f"HTTP Error: {err}")

#     # def test_delete_customer(self):
#     #     customer_id = 'NEWCUST'  # Assuming the ID of the customer to be deleted

#     #     response = requests.delete(f'{base_url}/customers/{customer_id}')

#     #     try:
#     #         response.raise_for_status()
#     #         print(response.json())
#     #     except requests.exceptions.HTTPError as err:
#     #         print(f"HTTP Error: {err}")

    

    
# if __name__ == '__main__':
#     unittest.main()
import pytest
import requests

# Base URL of the Flask API
base_url = 'http://127.0.0.1:5000/'

def test_get_customers():
    response = requests.get(f'{base_url}/customers')
    assert response.status_code == 200

def test_add_customer():
    new_customer = {
        "CustomerID": "NEWCUST",
        "CompanyName": "New Company",
        "ContactName": "John Doe",
        "ContactTitle": "CEO",
        "Address": "123 Main St",
        "City": "Anytown",
        "Region": "Region",
        "PostalCode": "12345",
        "Country": "USA",
        "Phone": "555-1234",
        "Fax": "555-5678"
    }
    response = requests.post(f'{base_url}/customers', json=new_customer)
    assert response.status_code == 201

def test_update_customer():
    customer_id = 'NEWCUST'
    updated_customer_data = {
        "CompanyName": "Updated Company",
        "ContactName": "Jane Doe",
        "ContactTitle": "CTO",
        "Address": "456 Elm St",
        "City": "Othertown",
        "Region": "Region",
        "PostalCode": "54321",
        "Country": "Canada",
        "Phone": "555-9876",
        "Fax": "555-4321"
    }
    response = requests.put(f'{base_url}/customers/{customer_id}', json=updated_customer_data)
    assert response.status_code == 200

def test_delete_customer():
    customer_id = 'NEWCUST'
    response = requests.delete(f'{base_url}/customers/{customer_id}')
    assert response.status_code == 201
