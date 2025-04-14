from flask_wtf import FlaskForm
from flask import Flask, render_template, url_for, request, flash, redirect
from werkzeug.security import generate_password_hash
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, EmailField, IntegerField
from wtforms.validators import DataRequired
from data.reg_db import Reg_form
from data import db_session
class Form(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired()])
    name = StringField('Имя пользователя', validators=[DataRequired()])
    surname = StringField('Фамилия пользователя', validators=[DataRequired()])
    age = IntegerField('Возраст', validators=[DataRequired()])
    position = StringField("Должность", validators=[DataRequired()])
    speciality = StringField('Специальность', validators=[DataRequired()])
    address = TextAreaField('Адресс', validators=[DataRequired()])
    submit = SubmitField('Войти')



app = Flask(__name__)

with open('Token_text.txt', 'rt', encoding='utf-8') as op_f:
    token = op_f.read().strip()
app.config['SECRET_KEY'] = token

@app.route('/login',  methods=['GET', 'POST'])
def log():
    return 'Вы успешно прошли регистрацию!'
@app.route('/',  methods=['GET', 'POST'])
def in_db():
    form2 = Form()

    if form2.validate_on_submit():
        if form2.password.data != form2.password_again.data:
            return render_template('index.html', title='Регистрация',
                                   form=form2,
                                   message="(Пароли не совпадают)")
        else:

            new_user = Reg_form(
                email=form2.email.data,
                password=generate_password_hash(form2.password.data),
                name=form2.name.data,
                surname=form2.surname.data,
                age=form2.age.data,
                position=form2.position.data,
                speciality=form2.speciality.data,
                address=form2.address.data
            )

            db_sess = db_session.create_session()
            db_sess.add(new_user)
            db_sess.commit()
            return redirect('/login')
    return render_template('index.html', title='Регистрация', form=form2)





if __name__ == '__main__':
    db_session.global_init('db/blogs.db')
    app.run(port=8000, host='127.0.0.1', debug=True)

