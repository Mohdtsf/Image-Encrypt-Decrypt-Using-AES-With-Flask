from flask import Flask, request, render_template, redirect, send_file
from werkzeug.utils import secure_filename
import io

from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__, static_url_path="/static")
app.secret_key = 'aes-image-crypto-secret-key-change-in-production'
app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/about')
def about_page():
    return render_template('about.html')


# ==========================
# ENCRYPT ROUTE (IN-MEMORY)
# ==========================
@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    if request.method == 'POST':

        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']
        text = request.form['text']

        if file.filename == '':
            return redirect(request.url)

        if text == "":
            error = 'KEY REQUIRED !'
            return render_template('encrypt.html', error=error)

        if file and allowed_file(file.filename):

            filename = "enc_" + secure_filename(file.filename)

            # Generate AES key
            hash_obj = SHA256.new(text.encode('utf-8'))
            key = hash_obj.digest()

            # Read file in memory
            file_bytes = file.read()

            # Encrypt in memory
            encrypted_data = encryption(file_bytes, key)

            # Return encrypted file directly
            return send_file(
                io.BytesIO(encrypted_data),
                download_name=filename,
                as_attachment=True
            )

    return render_template('encrypt.html')


def encryption(message, key):
    message = pad(message)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(message)


# ==========================
# DECRYPT ROUTE (IN-MEMORY)
# ==========================
@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
    if request.method == 'POST':

        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']
        text = request.form['text']

        if file.filename == '':
            return redirect(request.url)

        if text == "":
            error = 'KEY REQUIRED !'
            return render_template('decrypt.html', error=error)

        if file and allowed_file(file.filename):

            filename = "dec_" + secure_filename(file.filename)

            # Generate AES key
            hash_obj = SHA256.new(text.encode('utf-8'))
            key = hash_obj.digest()

            # Read encrypted file in memory
            encrypted_bytes = file.read()

            # Decrypt in memory
            decrypted_data = decryption(encrypted_bytes, key)

            # Return decrypted file directly
            return send_file(
                io.BytesIO(decrypted_data),
                download_name=filename,
                as_attachment=True
            )

    return render_template('decrypt.html')


def decryption(ciphertext, key):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    return unpad(plaintext)


# ==========================
# PROPER PKCS7 PADDING
# ==========================
def pad(data):
    pad_length = AES.block_size - len(data) % AES.block_size
    return data + bytes([pad_length]) * pad_length


def unpad(data):
    pad_length = data[-1]
    return data[:-pad_length]
