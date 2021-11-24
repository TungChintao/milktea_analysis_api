import os
from dotenv import load_dotenv
# from flask_script import Manager
# from flask_migrate import MigrateCommand

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

# 必须卸载dotenv加载完环境变量之后
from app import create_app

app = create_app("production")
# manager = Manager(app)
# manager.add_command("db", MigrateCommand)
if __name__ == "__main__":
    app.run()


