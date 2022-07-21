import os

#konfigurasi aplikasi
SECRET_KEY="richal12345" # secret key aplikasi
PASSWORD_ROOT = '12345' # password sakti aplikasi buat by pass login

#jika menggunakan SQL ALCHEMY(ORM)
SQLALCHEMY_TRACK_MODIFICATIONS=False
# SQLALCHEMY_DATABASE_URI="postgresql://<user>:<password>@<host>:<port>/<sid>"

USER_POSTGRES_DB = "qupohtldjghryt"
PASSWORD_POSTGRES_DB = "f3f02f540be60dddc3130f7b97fe295509e7fb36ae6d00fef9ff0018201ab8e7"
HOST_POSTGRES_DB = "ec2-18-214-35-70.compute-1.amazonaws.com"
PORT_POSTGRES_DB = "5432"
DATABASE_POSTGRES_DB = "def8qdibhao4uk"

FILE_UPLOADS = "./static/richal_test/file"
FILE_BUKTI_SEWA = "./static/richal_test/file_bukti_sewa"
