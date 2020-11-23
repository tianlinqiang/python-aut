# -*- coding: UTF-8 -*-

from flask import Flask, request
import bin
import json


def getcontent(inputData):
    a = bin.get_table(inputData)
    return a


app = Flask(__name__)
@app.route("/index1" ,methods=['GET'])
def indextest():
    mouth = request.args.get("mouth")
    if mouth and len(mouth)==6:
        data1 = getcontent(mouth)
        return json.dumps(data1, ensure_ascii=False, indent=4)
    elif mouth and len(mouth)>6:
        mouth = str(mouth).split(",")
        data1 = getcontent(mouth)
        return json.dumps(data1, ensure_ascii=False, indent=4)
    else:
    exit("input mouth error.")




if __name__ == "__main__":
app.run(host='0.0.0.0', port=5590)


