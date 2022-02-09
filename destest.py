from calendar import c
from App.models import Candidacy, Users
from App import db, app
import pandas as pd
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
#print(Candidacy.query.join(Users).with_entities(Candidacy.*, Users.first_name).first())

#print(Candidacy.query.join(Users).with_entities(Users.first_name,Candidacy.entreprise, Candidacy.contact_full_name, Candidacy.contact_email, Candidacy.contact_mobilephone,Candidacy.date,Candidacy.status).all())

# u = Candidacy.query.filter(Candidacy.status == "En cours").all()
# print(u)

# l = list(set([u[i].user_id for i in range(0,len(u))]))

# names = Candidacy.query.all()
# df = pd.read_sql_query(names, db.session.bind)

# print(df)

#test2 = [comp.company for comp in test]
 


# comp = [{"company" : c.company} for c in Candidacy.query.group_by("company").all()]
# print(comp[0]["company"])

# print('REQUETE ADMIN', Candidacy.get_all_in_list_with_user_name())
# print(Candidacy.find_by_user_id(1))

def sample_metadata(database):
    """Return the MetaData for a given sample."""
    with app.app_context():
        sel = [
            Candidacy.user_id,
            Candidacy.company,
            Candidacy.job_type,
            Candidacy.contact_full_name,
            Candidacy.contact_email,
            Candidacy.contact_mobilephone,
            Candidacy.date,
            Candidacy.status,
            Candidacy.origin,
            Candidacy.description,
            Candidacy.comment,
        ]
        
        results = db.session.query(*sel).all()

        # Create a dictionary entry for each row of metadata information
        sample_metadata = {}
        for result in results:
            sample_metadata["user_id"] = result[0]
            sample_metadata["company"] = result[1]
            sample_metadata["job_type"] = result[2]
            sample_metadata["contact_full_name"] = result[3]
            sample_metadata["contact_email"] = result[4]
            sample_metadata["contact_mobilephone"] = result[5]
            sample_metadata["date"] = result[6]
            sample_metadata["status"] = result[7]
            sample_metadata["origin"] = result[8]
            sample_metadata["description"] = result[9]
            sample_metadata["comment"] = result[10]

        print(sample_metadata)
        return jsonify(sample_metadata)
sample_metadata(db)