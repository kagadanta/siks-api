# SIKS - API

SIKS API - Sistem Informasi Kelola Stok API

## Memulai

Instruksi ini berisi tentang bagaimana menjalankan aplikasi ini 
pada komputer lokal Anda untuk tujuan pengembangan dan pengujian.

### Prasyarat

Project ini dikembangkan dengan:

- Windows 7
- Python 3.6
- Django 3
- Django Rest Framework

### Instalasi
> Disarankan menggunakan virtual environment.

Clone project ini, masuk ke direktori project. Ketik:

```
pip install -r requirements.txt
```

Lakukan migrasi:

```
python manage.py migrate
```

> Project ini menggunakan database default (`SQLite`),
> Anda bisa mengubahnya sesuai kebutuhan di `settings.py`.

Buat superuser baru:

```
python manage.py createsuperuser
```

Jalankan development server:

```
python manage.py runserver
```

Akses `http://localhost:8000`.

## Kontribusi

Silahkan pull request. Jika ada perubahan besar, pastikan membuat issue 
untuk diskusi.

## Versi

Project ini menggunakan **Semantic Versioning** (SemVer).

## License

Project ini dilisensikan di bawah Lisensi MIT.
