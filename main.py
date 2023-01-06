import functions_framework
import os
@functions_framework.http
def main(request):
   # Get TOKEN from environment variable
   TOKEN = os.environ.get('TOKEN')
   return f'TOKEN: {TOKEN}!'
