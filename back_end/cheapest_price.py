import requests
from bs4 import BeautifulSoup

# Set the User-Agent header to mimic a web browser
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/85.0.4183.121 Safari/537.36"
}

def jumia_most_cheap(product_name):
    try:
        # Construct the URL for the search query on Jumia
        jumia_sorted_link = f"https://www.jumia.co.ke/catalog/?q={product_name}"

        # Send a GET request to the Jumia URL and retrieve the HTML content
        page_html = requests.get(jumia_sorted_link, headers=header).text

        # Create a BeautifulSoup object to parse the HTML content
        soup = BeautifulSoup(page_html, 'html.parser')

        # Find all div elements containing the product information
        divs = soup.find_all('div', class_='info')

        # Create an empty list to store the product information
        products = []

        # Loop over each div element and extract the name, price, and link
        for div in divs:
            name = div.find('h3', class_='name').text.strip()
            price_text = div.find('div', class_='prc').text.strip()
            price_in_ksh = float(price_text.split(' ')[-1].replace(',', ''))  # Extract the numeric part of the price
            exchange_rate_ksh_to_usd = 0.009
            price_in_usd = price_in_ksh * exchange_rate_ksh_to_usd
            link = jumia_sorted_link

            # Create a dictionary to store the product information
            product = {
                "Website": "JUMIA",
                "Name": name,
                "Price": price_in_usd,
                "Link": link
            }

            # Append the product dictionary to the products list
            products.append(product)

        return products
    except Exception as e:
        print(f"An error occurred while scraping Jumia: {e}")
        return []

def flipkart_most_cheap(product_name):
    try:
        # Construct the URL for the search query on Flipkart
        flipkart_sorted_link = f"https://www.flipkart.com/search?q={product_name}"

        # Send a GET request to the Flipkart URL and retrieve the HTML content
        page_html = requests.get(flipkart_sorted_link, headers=header).text

        # Create a BeautifulSoup object to parse the HTML content
        soup = BeautifulSoup(page_html, 'html.parser')

        # Find all div elements containing the product information
        divs = soup.find_all('div', class_='_1AtVbE col-12-12')

        # Create an empty list to store the product information
        products = []

        # Loop over each div element and extract the name, price, and link
        for div in divs:
            name = div.find('a', class_='_4rR01T').text.strip()
            price = div.find('div', class_='_30jeq3 _1_WHN1').text

            if price:
                price_text = price.text.strip()
                price_in_inr = float(price_text.replace(',', ''))
                price_in_usd = price_in_inr / 83  # Convert INR to USD using an approximate rate
                link = 'https://www.flipkart.com' + div.find('a', class_='IRpwTa')['href']
            # Create a dictionary to store the product information
            product = {
                "Website": "Flipkart",
                "Name": name,
                "Price": price_in_usd,
                "Link": link
            }

            # Append the product dictionary to the products list
            products.append(product)

        return products
    except Exception as e:
        print(f"An error occurred while scraping Flipkart: {e}")
        return []

def amazon_most_cheap(product_name):
    try:
        # Construct the URL for the search query on Amazon
        amazon_sorted_link = f"https://www.amazon.com/s?k={product_name}"

        # Send a GET request to the Amazon URL and retrieve the HTML content
        page_html = requests.get(amazon_sorted_link, headers=header).text

        # Create a BeautifulSoup object to parse the HTML content
        soup = BeautifulSoup(page_html, 'html.parser')

        # Find all div elements containing the product information
        divs = soup.find_all('div', class_='sg-col-inner')

        # Create an empty list to store the product information
        products = []

        # Loop over each div element and extract the name, price, and link
        for div in divs:
            name = div.find('span', class_='a-size-medium a-color-base a-text-normal').text.strip()
            price = div.find('span', class_='a-offscreen').text.strip().replace('€ ', '')
            link = 'https://www.amazon.com' + div.find('a', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')['href']

            # Create a dictionary to store the product information
            product = {
                "Website": "Amazon",
                "Name": name,
                "Price": price,
                "Link": link
            }

            # Append the product dictionary to the products list
            products.append(product)

        return products
    except Exception as e:
        print(f"An error occurred while scraping Amazon: {e}")
        return []

def alibaba_most_cheap(product_name):
    try:
        # Construct the URL for the search query on Alibaba
        alibaba_sorted_link = f"https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText={product_name}"

        # Send a GET request to the Alibaba URL and retrieve the HTML content
        page_html = requests.get(alibaba_sorted_link, headers=header).text

        # Create a BeautifulSoup object to parse the HTML content
        soup = BeautifulSoup(page_html, 'html.parser')

        # Find all div elements containing the product information
        divs = soup.find_all('div', class_='JIIxO')

        # Create an empty list to store the product information
        products = []

        # Loop over each div element and extract the name, price, and link
        for div in divs:
            name = div.find('h4', class_='elements-title-normal__content').text.strip()
            price = div.find('p', class_='elements-offer-price-normal medium').replace('US $', '')
            link = div.find('a', class_='elements-title-normal__link')['href']

            # Create a dictionary to store the product information
            product = {
                "Website": "Alibaba",
                "Name": name,
                "Price": price,
                "Link": link
            }

            # Append the product dictionary to the products list
            products.append(product)

        return products
    except Exception as e:
        print(f"An error occurred while scraping Alibaba: {e}")
        return []

# Function to compare the prices of products on different websites
def best_price_sorted_list(product_name):
    try:
        # Get the cheapest product information from each website
        jumia_info = jumia_most_cheap(product_name)
        flipkart_info = flipkart_most_cheap(product_name)
        amazon_info = amazon_most_cheap(product_name)
        alibaba_info = alibaba_most_cheap(product_name)

        # Combine the product information from all websites
        products = jumia_info + flipkart_info + amazon_info + alibaba_info

        # Convert the prices from string to float
        for product in products:
            product['Price'] = float(product['Price'])

        # Sort the products based on the price in ascending order
        sorted_products = sorted(products, key=lambda x: x['Price'])

        return sorted_products
    except Exception as e:
        print(f"An error occurred while comparing prices: {e}")
        return []

