# 🔐 AES Image Encryption & Decryption

A Flask web application that encrypts and decrypts images using the **AES-256 (CBC mode)** symmetric encryption algorithm. Upload any image, provide a secret key, and download the encrypted file — then decrypt it later with the same key.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.x-000000?logo=flask)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Features

- **Image Encryption** — Upload an image (PNG, JPG, JPEG, GIF) and encrypt it with a secret key using AES-256
- **Image Decryption** — Restore encrypted images back to their original form using the same key
- **Modern Dark UI** — Sleek cyberpunk-inspired interface with glassmorphism, gradient animations, and responsive design
- **Drag & Drop Upload** — Intuitive file upload area with visual feedback
- **Secure Hashing** — Keys are hashed with SHA-256 before use, so any passphrase works
- **Instant Download** — Encrypted/decrypted files are automatically downloaded after processing

---

## 🛠️ Tech Stack

| Layer      | Technology                          |
|------------|-------------------------------------|
| Backend    | Python, Flask                       |
| Encryption | PyCryptodome (AES-256 CBC)          |
| Frontend   | HTML5, CSS3, Bootstrap 5.3          |
| Icons      | Font Awesome 6                      |
| Typography | Google Fonts (Inter)                |

---

## 📁 Project Structure

```
├── app.py                  # Flask application with encrypt/decrypt logic
├── requirements.txt        # Python dependencies
├── wsgi.py                 # WSGI entry point
├── vercel.json             # Vercel deployment config
├── templates/
│   ├── base.html           # Shared layout (navbar, footer)
│   ├── home.html           # Landing page with feature cards
│   ├── encrypt.html        # Encryption form
│   ├── decrypt.html        # Decryption form
│   └── about.html          # AES algorithm explanation
├── static/
│   └── styles/
│       └── main.css        # Custom design system
├── uploads/                # Temporary uploaded files (auto-created)
└── downloads/              # Processed files for download (auto-created)
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Mohdtsf/Image-Encrypt-Decrypt-Using-AES-With-Flask.git
   cd Image-Encrypt-Decrypt-Using-AES-With-Flask
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   flask run
   ```
   The app will start at **http://localhost:5000**

### Alternative: Run with Python directly
```bash
python -c "from app import app; app.run(debug=True)"
```

---

## 📖 How to Use

### Encrypting an Image
1. Navigate to the **Encrypt** page
2. Click the upload area to select an image (PNG, JPG, JPEG, or GIF)
3. Enter a **secret key** (any passphrase — it will be hashed with SHA-256)
4. Click **Encrypt Image**
5. The encrypted file will automatically download

### Decrypting an Image
1. Navigate to the **Decrypt** page
2. Upload the **encrypted file** you received earlier
3. Enter the **same secret key** used during encryption
4. Click **Decrypt Image**
5. The original image will automatically download

> ⚠️ **Important:** You must use the exact same key for decryption that was used for encryption. If the key doesn't match, the output will be corrupted.

---

## 🔒 How AES Encryption Works

1. Your passphrase is hashed with **SHA-256** to produce a 256-bit key
2. A random **Initialization Vector (IV)** is generated for each encryption
3. The image bytes are padded and encrypted using **AES-256 in CBC mode**
4. The IV is prepended to the ciphertext for use during decryption
5. During decryption, the IV is extracted, and the original bytes are restored

---

## 📦 Dependencies

- **Flask** — Web framework
- **PyCryptodome** — AES encryption/decryption
- **Werkzeug** — Secure file handling

Install all with:
```bash
pip install flask pycryptodome werkzeug
```

---

## 🌐 Deployment

The project includes a `vercel.json` for deployment on [Vercel](https://vercel.com). You can also deploy to any platform that supports Python WSGI apps (Heroku, Railway, Render, etc.).

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## Developed By

Mohd Tauseef Ansari
