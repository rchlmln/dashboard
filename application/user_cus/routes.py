from flask import request, render_template, make_response, request, jsonify, session, redirect, url_for, send_from_directory, Blueprint, flash
from flask_login import current_user, login_required
from datetime import date
import json, requests, hashlib
import csv
import pandas as pd
import os
from application import app
from application.dbdvd import *

user_cus = Blueprint('user_cus', __name__)

@user_cus.route("/user_cus", methods=['GET'])
@login_required
def detail_user():

    no_kta = current_user.id    # print(no_kta)

    dataDetailUser = getDetailUser(no_kta)
    # print(dataDetailUser)

    return render_template('user_cus/detail_user.html', title='Detail Update User', dataDetailUser = dataDetailUser['result'])  



@user_cus.route("/user_cus/proses_update", methods=['POST'])
@login_required
def proses_update_user():

    today = date.today()
    tgl_update = today
    user_update = current_user.id

    no_kta = request.form.get('no_kta', None)
    nama = request.form.get('nama', None)
   

    # print(role_f)
    pin = request.form.get('pin', None)
  
    # print(status_aktif)

    response = proses_update_cus(nama, pin, user_update, tgl_update, no_kta)
    # print(response)


    return response
    


    

	
