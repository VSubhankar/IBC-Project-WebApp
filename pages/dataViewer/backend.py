# backend.py

web_address_dict = {
    '10:45:25_31/11/2023': 'https://drive.google.com/file/d/1x7kGrvH08GLEsdJMcFj12ceEs3bzeRWb/preview',
    # Add more button-web address mappings as needed
}

def fetch_web_address(button_name):
    web_address = web_address_dict.get(button_name)
    if web_address is not None:
        return web_address
    else:
        raise ValueError('Button not found')
