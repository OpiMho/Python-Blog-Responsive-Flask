
## Blog in Python with Flask & Mongo [RESPONSIVE]

### Jugando cree un blog en flask, rapido y sencillo. 

![](https://cdn.apkgoogle.org/storage/2020/09/Python-3-Tutorials-Learn-Python-Tutorials-Full-Ad-Free-MoD-APK-3.3.png)

 ![](https://img.shields.io/badge/Version-1.25-black) 


**Date: 2019 | Python 3.6 | Flask 1.0.3 **
`$ pip3 -r requirements.txt`

----



![Responsive](https://i.imgur.com/f5J45dj.png)
<br>
##### MongoDB configuracion. 
[RECOMENDADO: Tutorial de SQLAlchemy](https://j2logo.com/python/sqlalchemy-tutorial-de-python-sqlalchemy-guia-de-inicio/)
```
 Archivo: ntp/ __init__.py
app.config['SECRET_KEY'] = ''"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DIGITALALCHIMIST.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
```

####  Campos de la db.

```
//Usuario:
id = db.Column(db.Integer, primary_key=True)<br>
username = db.Column(db.String(20), unique=True, nullable=False)<br>
image_file = db.Column(db.String(20), nullable=False,default='default.jpg')<br>
password = db.Column(db.String(60), nullable=False)<br>
posts = db.relationship('Post', backref='author', lazy=True)<br>
//Password:
id = db.Column(db.Integer, primary_key=True)<br>
    title = db.Column(db.String(100), nullable=False)<br>
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)<br>
    content = db.Column(db.Text, nullable=False)<br>
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
//Comentarios 
id = db.Column(db.Integer, primary_key=True)<br>
    postId = db.Column(db.Integer, nullable=False)<br>
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)<br>
    comment = db.Column(db.Text, nullable=False)<br>
    user_id = db.Column(db.Text, db.ForeignKey('user.id'), nullable=False)

```







