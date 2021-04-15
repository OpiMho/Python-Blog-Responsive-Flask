### Blog in Python with Flask & Mongo [RESPONSIVE]. 
Date: 2019 by OpiMho | Python 3.6 | Flask 1.0.3 <br>
$ pip3 -r requirements.txt
<br/><br/>
#MongoDB configuracion. <br>
<code>
#### Archivo: __init__.py<br>
app.config['SECRET_KEY'] = ''<br>
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DIGITALALCHIMIST.db'<br>
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False<br>
</code>
<br>

### Campos de Usuario de la db de Blog
<code>
id = db.Column(db.Integer, primary_key=True)<br>
username = db.Column(db.String(20), unique=True, nullable=False)<br>
image_file = db.Column(db.String(20), nullable=False,default='default.jpg')<br>
password = db.Column(db.String(60), nullable=False)<br>
posts = db.relationship('Post', backref='author', lazy=True)<br>

</code>
<br>

### Campos de Posts de la db de Blog
<code>
id = db.Column(db.Integer, primary_key=True)<br>
    title = db.Column(db.String(100), nullable=False)<br>
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)<br>
    content = db.Column(db.Text, nullable=False)<br>
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

</code>
<br>

### Campos de Comentarios de los Posts de la db de Blog
<code>
id = db.Column(db.Integer, primary_key=True)<br>
    postId = db.Column(db.Integer, nullable=False)<br>
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)<br>
    comment = db.Column(db.Text, nullable=False)<br>
    user_id = db.Column(db.Text, db.ForeignKey('user.id'), nullable=False)

</code>
<br>
<br>

# TD;LR

## [ScreenShot]

<br>

![Responsive](https://i.imgur.com/f5J45dj.png)

Bye! Love all.