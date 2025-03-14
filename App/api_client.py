
import requests
api_url = 'http://127.0.0.1:8000/'

def AllProducts():
    response = requests.get(api_url + 'products/countproduct/')
    print('staus code is',response.status_code)
    if response.status_code == 200:
        print('working')
        return response.json()
    else:
        print('not working')
        return None

def Products():
    response = requests.get(api_url + 'products/products/')
    print('staus code is',response.status_code)
    if response.status_code == 200:
        print('working')
        return response.json()
    else:
        print('not working')
        return None
    
# print(get_data())

def Edit_Products():
    response = requests.put(api_url + 'products/editproduct/')
    print('staus code is',response.status_code)
    if response.status_code == 200:
        print('working')
        return response.json()
    else:
        print('not working')
        return None
    
# print(get_data())

def Users():
    response = requests.get(api_url + 'users/users/')
    print('staus code is',response.status_code)
    if response.status_code == 200:
        print('working')
        return response.json()
    else:
        print('not working')
        return None
    
# print(get_data())

# def Login():
#     # {
#     #     "detail": "Method \"GET\" not allowed."
#     # }
#     loginurl = requests.get(api_url + 'users/login/')
#     response = requests.post(api_url + 'users/login/')
#     if response.status_code == 200:
#         print('working')
#         return response.json()
#     else:
#         print('not working')
#         return None
    
# # print(get_data())




