import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("C:\\FirebaseCreds\\creds.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
db.collection('person').add({'name':'aysuh', 'age': 21})
db.collection('person').add({'name':'ramya', 'age': 20})