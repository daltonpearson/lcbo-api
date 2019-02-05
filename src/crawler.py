import xml.etree.ElementTree as ET
import requests

API_BASE_URL = 'http://www.foodanddrink.ca/lcbo-webapp/'
NUM_PRODUCTS = 5#15000

def products(num_products):

    products_url = f"productsearch.do?numProducts={num_products}"
    response = requests.get(f'{API_BASE_URL}{products_url}')
    response_string = response.content
    response_xml = ET.fromstring(response_string)
    products = response_xml.findall("./products/product/itemNumber")
        
    product_ids = [product.text for product in products]

    return product_ids

def product(product_id):

    products_url = f"productdetail.do?itemNumber={product_id}"
    response = requests.get(f'{API_BASE_URL}{products_url}')
    response_string = response.content
    response_xml = ET.fromstring(response_string)
    
    product_xml = response_xml.find("./products/product")
    
    product = {
            'beer_path':f'http://www.lcbo.com/lcbo/search?searchTerm={product_xml.find("./itemNumber").text}',
            'name': product_xml.find("./itemName").text,
            'category': product_xml.find("./liquorType").text,
            'percent': product_xml.find("./alcoholPercentage").text,
            #'is_ocb':data['result']['is_ocb'],
            #'max_alc_per_dollar':0.00
            }

    return product

product_ids = products(5)
print(product_ids)
for product_id in product_ids:
    print(str(product(product_id)))
