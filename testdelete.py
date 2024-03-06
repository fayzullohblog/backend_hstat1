import shutil

import os

venv_path = os.environ.get('VIRTUAL_ENV')
if venv_path:
    print("venv muhiti joylashuvi:", venv_path)
else:
    print("venv muhiti topilmadi.")
