from flask import  render_template, url_for, flash, redirect, request, render_template_string
from ntp.models import User, Post, Comments
from ntp.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm, CommentForm, ChatForm
from ntp import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/")
def root():
    form=ChatForm()
    posts= Post.query.all()
    return render_template("home.html", posts=posts, form=form)

@app.route('/acerca')
def acerca():
    return render_template("nosotros.html")




@app.route("/registrarse", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('root'))
    form= RegistrationForm()
    if form.validate_on_submit():
        hashed_password =bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.usuario.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Tu cuenta fue creada!', 'success')
        return redirect(url_for('root'))
    return render_template('register.html', title='Registro', form=form)

@app.route("/login", methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('root'))
    form= LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('root'))
        else:
             flash('No te pudiste loguear, revisa tus credenciales.','danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('root'))

@app.route("/cuenta" , methods=['GET','POST'])
@login_required
def cuenta():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Tu cuenta ha sido actualizada!', 'success')
        return redirect(url_for('cuenta'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    return render_template('cuenta.html', title='Cuenta', form=form)

@app.route("/post/nuevo" , methods=['GET','POST'])
@login_required
def post_nuevo():
    form=PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Tu post ha sido posteado!', 'success')
        return redirect(url_for('root'))
    return render_template('crear_post.html', title='Crear Post', form=form, legend='Crear Post')

@app.route("/post/<int:post_id>", methods=['GET','POST'])
def post(post_id):
    post = Post.query.get_or_404(post_id)
    comment = Comments.query.filter_by(postId=post_id).all()
    int_post = int(post_id)
    form = CommentForm()
    if form.validate_on_submit():
        comment = Comments(postId=int_post, comment=form.comment.data, user_id=current_user.username)
        db.session.add(comment)
        db.session.commit()
        flash('Tu comentario ha sido posteado!', 'success')
        return redirect(request.url)
    return render_template('post.html', title=post.title, post=post, comments=comment, form=form)

