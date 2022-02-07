# candi-app
Interface pour candidature



# Deployment:

La version en production utilise Postgre SQL.
Attention la dernière version de SQLAlchemy n'est pas compatible avec Heroku, il faut utiliser la version dans les requirements.
Après avoir push sur Heroku, il faut accèder à la console du serveur et initialiser la db: python create.py
