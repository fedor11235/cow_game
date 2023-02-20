import sqlite3, os
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
API_TOKEN = os.getenv('API_TOKEN')

app = Flask(__name__)

@app.route('/', methods=['GET'])
def set_user_score():
  return render_template('index.html')

def main():
  app.run(debug=True, host=HOST, port=PORT)

if __name__ == '__main__':
  main()