import os
import ProxyCloud

BOT_TOKEN =  os.environ.get('bot_token','5876467688:AAEabu0owp9btVuVgGnTkOU9gW0p2XQ6M_A')
API_ID =  os.environ.get('api_id','17158127')
API_HASH = os.environ.get('api_hash','d1a5974070430293b64fde5339591447')
SPLIT_FILE = 1024 * 1024 * int(os.environ.get('split_file','99'))
ROOT_PATH = 'root/'
ACCES_USERS = os.environ.get('tl_admin_user','JAGB2021').split(';')
PROXY = ProxyCloud.parse(os.environ.get('proxy_enc','http://KFGGJJYGJKLHFKYEDIGDYJJEKEFKREEGLFDKLH'))

if PROXY:
  print(f'Proxy {PROXY.as_dict_proxy()}')
