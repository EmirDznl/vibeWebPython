# Django Projesi Kurulumu

Bu proje Django ile geliştirilmiş bir web uygulamasıdır. Aşağıdaki adımları takip ederek projeyi kendi bilgisayarınızda çalıştırabilirsiniz.

```bash
# Repository'yi klonlayın
git clone https://github.com/kullanici_adi/proje_adi.git
cd proje_adi

# Sanal ortam oluşturun (önerilir)
python -m venv venv

# Linux / MacOS
source venv/bin/activate
# Windows
# venv\Scripts\activate

# Gerekli paketleri yükleyin
pip install -r requirements.txt

# Veritabanı işlemleri
python manage.py makemigrations
python manage.py migrate

# Sunucuyu çalıştırın
python manage.py runserver

