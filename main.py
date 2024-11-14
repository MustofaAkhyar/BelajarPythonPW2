import os
import time
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/fakultas')
def fakultas():
    fakultas = ["FIKR", "FEB"]
    return render_template('fakultas.html', fakultas=fakultas)

@app.route('/prodi')
def prodi():
    prodi = [
        {"nama" : "informatika", "fakultas" : "FIKR"},
        {"nama" : "sistem informasi", "fakultas" : "FIKR"},
        {"nama" : "akuntansi", "fakultas" : "FEB"},
        {"nama" : "manajemen", "fakultas" : "FEB"}
    ]
    return render_template('prodi.html', prodi=prodi)

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    if request.method == 'POST':
        nama = request.form['nama']
        email = request.form['email']
        pesan = request.form['pesan']
        # print(f"Nama : {nama} \n Email : {email} \n Pesan : {pesan}")

        pesan_konfirmasi = f"thankyou, {nama}. pesanmu berhasil dikirim"
        return render_template('contact.html', pesan_konfirmasi=pesan_konfirmasi, nama=nama, email=email, pesan=pesan)
        
    return render_template('contact.html')

@app.route('/registrasi', methods = ['GET', 'POST'])
def registrasi():
    if request.method == 'POST':
        nisn = request.form['nisn']
        nama = request.form['nama']
        email = request.form['email']
        tanggal_lahir = request.form['tanggal_lahir']
        asal_sekolah = request.form['asal_sekolah']
        pilihan_prodi = request.form['pilihan_prodi']
        
        # Cek jika ada file yang diunggah
        foto = request.files['foto']
        if foto:
            # Mengambil timestamp saat ini untuk menambahkan ke nama file
            timestamp = str(int(time.time()))
             # Mengambil ekstensi file asli
            ext = foto.filename.split('.')[-1]

            # Menambahkan ekstensi ke nama file unik
            unique_filename = f"{timestamp}.{ext}"

            # Menyimpan file dengan nama unik
            foto_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
            foto.save(foto_path)
            foto_path = f'uploads/{unique_filename}'  # Menyimpan path relatif dengan menggunakan '/uploads/'
        else:
            foto_path = None

        
        

        pesan_konfirmasi = f"thankyou, {nama}. pesanmu berhasil dikirim"
        return render_template('registrasi.html', 
        pesan_konfirmasi=pesan_konfirmasi, nama=nama, email=email, nisn=nisn, 
        tanggal_lahir=tanggal_lahir, asal_sekolah=asal_sekolah, pilihan_prodi=pilihan_prodi, foto=foto_path)
        
    return render_template('registrasi.html')



if __name__ == '__main__':
    app.run(debug=True)