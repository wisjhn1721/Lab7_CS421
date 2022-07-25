from flask import Flask, render_template, flash
from forms import PasswordForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'securityKey'


@app.route('/', methods=['GET', 'POST'])
def home():
    form = PasswordForm()
    return render_template('home.html', form=form)


@app.route('/check', methods=['GET', 'POST'])
def check():
    form = PasswordForm()
    if form.validate_on_submit():
        pw = form.password.data
        err = False
        print("checking the password: ", pw)
        if len(pw) < 8:
            flash("Password must be 8 characters or longer", category='error')
            err = True

        hasUpper = False
        hasLower = False
        for char in pw:
            if char.isupper():
                hasUpper = True
            elif char.islower():
                hasLower = True

        if not (hasUpper and hasLower):
            err = True

        if not hasUpper:
            flash('Password must contain an uppercase letter', category='error')
        if not hasLower:
            flash('Password must contain an lowercase letter', category='error')

        lastChar = pw[len(pw)-1]
        if not lastChar.isdigit():
            err = True
            flash('Password must end with a number', category='error')

        if not err:
            flash("Password met all requirements, yayy!", category='success')

        print("The last character in the password is: ", pw[len(pw)-1])
    return render_template('report.html')


if __name__ == '__main__':
    app.run()
