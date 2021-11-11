import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

# 必须卸载dotenv加载完环境变量之后
from app import create_app

app = create_app()
app.run()
