from dotenv import load_dotenv
import os
from supabase.client import create_client

load_dotenv('.env')

client = create_client(os.getenv('SUPABASE_URL', ''), os.getenv('SUPABASE_SECRET_KEY', ''))

