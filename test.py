# test_env.py
import os
from dotenv import load_dotenv

# Load with verbose to see what's happening
load_dotenv(verbose=True)

# Try to get the key
api_key = os.getenv('OPENAI_API_KEY')
print(f"API Key found: {'✅' if api_key else '❌'}")
if api_key:
    print(f"Key starts with: {api_key[:10]}...")
else:
    print("❌ No API key found")
    
# Show all variables loaded
print("\nAll environment variables:")
for key, value in os.environ.items():
    if 'OPENAI' in key.upper() or 'API' in key.upper():
        print(f"  {key} = {value[:20] if value else 'None'}...")