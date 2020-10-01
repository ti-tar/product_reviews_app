import os
import sys
from dotenv import load_dotenv
from pathlib import Path

if os.path.isfile('.env'):
    print('Environment vars is loading. file: `.env`')
    filepath = os.path.join(str(Path().cwd()), '.env')

    if load_dotenv(dotenv_path=filepath, override=True):
        print('ENV `.env` loaded')
    else:
        sys.exit('Error occurred during loading env file.')