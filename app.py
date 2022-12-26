from flask import Flask, request
import platform
import psutil
import requests
import sys 
app = Flask(__name__)

def controller_status():
    return  {'status':'server is running','S.O. ':sys.platform,'Python Ver.:':sys.version}, 200 

def controller_poke(headers):
    try:
        ability_name = headers["ability_name"]
        endpoint_poke_api = headers["endpoint_poke_api"]
        response = requests.get(endpoint_poke_api).json()
        for ability in response["abilities"]:
            if (ability["ability"]["name"] == ability_name):
                return {"status": "success", "has_ability": True}, 200
    except KeyError:
        return {"status Url ": "error", "message": "invalid URL"}, 400
    except Exception as err:
        return {"status": "error", "message": err.args[0]}, 400

    return {"status": "success", "has_ability": False}, 200

@app.route('/')
def root():
    return 'Hi Demo Poke Api'

@app.route('/status', methods=['GET'])
def status():
    res = controller_status()
    return res

@app.route('/poke', methods=['GET'])
def has_ability():
    res = controller_poke(request.headers)
    return res

if __name__ == '__main__':
    app.run(host="localhost", port=3000, debug=True)