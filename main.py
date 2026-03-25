from flask_wtf import FlaskForm, render_template
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'some_secret_key'

class DoubleForm(FlaskForm):
    user_id = StringField('id астронавта', validators=[DataRequired()])
    user_password = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id = StringField('id капитана', validators=[DataRequired()])
    password = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = DoubleForm()
    if form.validate_on_submit():
        id_cap = form.id.data
        password_cap = form.password.data
        return render_template('doubleform.html', title='Доступ разрешен!', access='True', id=id_cap, password=password_cap)
    return render_template('doubleform.html', title='Двойная авторизация', access='False')

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
