def get_links(product_name):
    amazon_link = f"https://www.amazon.co.uk/s?k={product_name}"
    jumia_link = f"https://www.jumia.co.ke/catalog/?q={product_name}"
    hepsiburada_link = f"https://www.hepsiburada.com/ara?q={product_name}&kategori=2147483642_371965"
    alibaba_link = f"https://www.alibaba.com/trade/search?tab=all&searchText={product_name}"
    flipkart_link = f"https://www.flipkart.com/search?q={product_name}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

    website_links = {
        "amazon": amazon_link,
        "jumia": jumia_link,
        "hepsiburada": hepsiburada_link,
        "alibaba": alibaba_link,
        "flipkart": flipkart_link,
    }

    return website_links

