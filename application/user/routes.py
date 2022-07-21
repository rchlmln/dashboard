from flask import request, render_template, make_response, request, jsonify, session, redirect, url_for, send_from_directory, Blueprint, flash
from flask_login import current_user, login_required
from datetime import date
import json, requests, hashlib
import csv
import pandas as pd
import os
from application import app
from application.dbdvd import *

user = Blueprint('user', __name__)

@user.route('/user', methods=["GET", "POST"])
@login_required
def list_user():

    dataListUser = getListUser()
    kta = current_user.id
   
      
    return render_template('user/index.html', title='List User', dataListUser = dataListUser['result'] 
        )

@user.route("/user/detail_user", methods=['GET'])
@login_required
def detail_user():

    no_kta  = request.args['n']
    # print(no_kta)

    dataDetailUser = getDetailUser(no_kta)
    # print(dataDetailUser)

    return render_template('user/detail_user.html', title='Detail Update User', dataDetailUser = dataDetailUser['result'])  

@user.route('/user/hapus_user', methods=['POST'])
@login_required
def delete_user():


    inp = request.form
    print(inp['no_kta'])

    user_hapus = current_user.id
    if user_hapus != inp['no_kta']:
        today = date.today()
        tgl_update = today
        print(tgl_update)
        response = proses_hapus_user(user_hapus, tgl_update, inp['no_kta'])
        print(response)
        

    else:
        response = {
            'status': 'F',
            'message': 'Tidak Boleh Hapus User Sendiri'
            
        }

    return response

@user.route("/user/proses_update", methods=['POST'])
@login_required
def proses_update_user():

    today = date.today()
    tgl_update = today
    user_update = current_user.id

    no_kta = request.form.get('no_kta', None)
    nama = request.form.get('nama', None)
    role = request.form.get('role', None)
    if(role == "Admin"):
        flagr = "sys"
    elif(role == "Customer"):
        flagr = "cus" 
    role_f = flagr

    # print(role_f)
    pin = request.form.get('pin', None)
    status = request.form.get('status', None)
    # print(status)
    if(status == "Aktif"):
        flag = "T"
    elif(status == "Tidak Aktif"):
        flag = "F" 
    status_aktif = flag
    # print(status_aktif)

    response = proses_update(nama, role_f, pin, status_aktif, user_update, tgl_update, no_kta)
    # print(response)


    return response
    


    

	
