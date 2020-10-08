from flask import render_template, url_for, flash, redirect, request # import render_template function for rendering HTML pages individually, url 4 for finding files in the background
from fitnessAppFlask import app, db, bcrypt
from fitnessAppFlask.forms import RegistrationForm, LoginForm
from fitnessAppFlask.models import User, Calorie                            # Using models in views, DB needs to exist first
from flask_login import login_user, current_user, logout_user, login_required

posts = [
    {
        'author':'blah',
        'title':'post 1',
        'content':'first post',
        'date_created':'today'
    },
    {
        'author':'blah2',
        'title':'post 21',
        'content':'second post',
        'date_created':'today'
    }
]

@app.route('/')             # routes
@app.route('/home')            
def home_page():
    return render_template('home.html', title='Welcome', posts = posts)

@app.route('/about')         
def about_page():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])         
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home_page'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(name=form.name.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Welcome {0}, your account has been created!'.format(form.name.data), 'success')
        return redirect(url_for('login')) #redirect to function name of route
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])         
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home_page'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()                    # Check if email exists, grab user
        if user and bcrypt.check_password_hash(user.password, form.password.data):      # Compare User saved password with entered password
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')                                        # Grab url parameter
            return redirect(next_page) if next_page else redirect(url_for('home_page')) # Redirect to original page the user was trying to access
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')      
    return render_template('login.html', title='Login', form=form)

@app.route('/logout')         
def logout():
    logout_user()            
    return redirect(url_for('home_page'))


@app.route('/account')
@login_required         
def account():          
    return render_template('account.html', title='Account')