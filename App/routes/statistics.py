from flask import render_template, redirect, url_for, flash, request
from App import db, app
from datetime import date
from ..models import Users, Candidacy
from ..forms import Login, AddCandidacy, ModifyCandidacy, ModifyProfile
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
import pandas as pd 
import json 
import plotly
import plotly.express as px


@app.route('/statistics', methods=['GET', 'POST'])
@login_required
def show_stats():
    df = px.data.medals_wide()
    fig1 = px.bar(df,x='nation', y = ['gold', 'silver', 'bronze'], title ="Wide=Form Input" )
    fig1json = json.dumps(fig1, cls = plotly.utils.PlotlyJSONEncoder)
    
    return render_template("statistiques.html", title = "Stats", fig1json = fig1json)