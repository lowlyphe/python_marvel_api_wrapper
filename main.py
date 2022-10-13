from Marvel import Marvel
from dotenv import load_dotenv
import os
load_dotenv()
API_PUBLIC_KEY = os.getenv('API_PUBLIC_KEY')
API_PRIVATE_KEY = os.getenv('API_PRIVATE_KEY')

data = Marvel(API_PUBLIC_KEY, API_PRIVATE_KEY)
data.set_endpoint('characters')
data.set_modifier('limit', 1)
print(data.get_info()) 