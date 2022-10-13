from Marvel import Marvel
from dotenv import load_dotenv
import os
load_dotenv()
API_PUBLIC_KEY = os.getenv('API_PUBLIC_KEY')
API_PRIVATE_KEY = os.getenv('API_PRIVATE_KEY')

data = Marvel(API_PUBLIC_KEY, API_PRIVATE_KEY)
data.set_endpoint('comics')
data.set_sub_endpoint('comics')
data.set_modifier('title', 'storm')

print(data.get_info()) 