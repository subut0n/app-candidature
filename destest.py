from calendar import c
from App.models import Candidacy, Users
from App import db





#print(Candidacy.query.join(Users).with_entities(Candidacy.*, Users.first_name).first())

#print(Candidacy.query.join(Users).with_entities(Users.first_name,Candidacy.entreprise, Candidacy.contact_full_name, Candidacy.contact_email, Candidacy.contact_mobilephone,Candidacy.date,Candidacy.status).all())
mon_id = 23
u = Candidacy.query.filter(Candidacy.status == "En cours").all()

# l = list(set([u[i].user_id for i in range(0,len(u))]))
# print(Users.query.filter_by(id=l[0]).first().last_name)
# print(l)




# test = Candidacy.query.group_by("company").all()
# #test2 = [comp.company for comp in test]
# print(test)

# comp = [{"company" : c.company} for c in Candidacy.query.group_by("company").all()]
# print(comp[0]["company"])

# print('REQUETE ADMIN', Candidacy.get_all_in_list_with_user_name())
print(Users.query.all())
user_candidacy=Candidacy.get_all_in_list_with_user_name()
#Candidacy(user_id = 23, company = "IBM", contact_full_name = "jean", contact_email="jean@gmail.com",date= "2022-01-01").save_to_db()

u = Candidacy.query.order_by(Candidacy.date.asc()).all()


user_candidacy = Candidacy.query.join(Users).with_entities(Users.first_name, Candidacy.company, Candidacy.contact_full_name,Candidacy.date,Candidacy.status).order_by(Candidacy.date.asc()).all()
j = Candidacy.query.all()
print("test : ")
print(j)


choice = "En cours"
request = Candidacy.query.filter(Candidacy.status == choice).all()
list_app_id = list(set([request[i].user_id for i in range(0,len(request))]))
list_app = Users.query.filter(Users.id.in_(list_app_id)).all()
list_app2 = [app.json() for app in list_app]
print("test 2 :")
#print(list_app2[0].company)


test = Candidacy.query.join(Users).with_entities(Users.first_name,Candidacy.id,Candidacy.company).all()
print("test 3 : ")
print(type(test[0]))


test = Candidacy.query.all()
list = [t.json() for t in test]
print("test 3 :")
print(list)

test = Candidacy.query.with_entities(Candidacy.company).distinct()
test2 = [{"company" : c.company} for c in test]
print("test 5 :")
print(test2)
