from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True


@app.route("/welcome", methods=['POST'])
def welcome():
    user_name = request.form['user-name']
    create_pw = request.form['create-pw']
    confirm_pw = request.form['confirm-pw']
    enter_email = request.form['enter-email']
    email_segments = enter_email.split('@', 1)
    email_dots = enter_email.split('.', 1)

    if user_name.strip() == '':
        user_name_error = "Please enter a username"
        return redirect("/?user_name_error=" + user_name_error + '&user_name=' + user_name + '&enter_email=' + enter_email)

    if ' ' in user_name:
        user_name_error = "Username cannot contain spaces"
        return redirect("/?user_name_error=" + user_name_error + '&user_name=' + user_name + '&enter_email=' + enter_email)

    if len(user_name) > 20 or len(user_name) < 3:
        user_name_error = "Username must be between 3 and 20 characters"
        return redirect("/?user_name_error=" + user_name_error + '&user_name=' + user_name + '&enter_email=' + enter_email)

    if create_pw.strip() == '':
        create_pw_error = "Please enter a password"
        return redirect("/?create_pw_error=" + create_pw_error + '&user_name=' + user_name + '&enter_email=' + enter_email)

    if ' ' in create_pw:
        create_pw_error = "Password cannot contain spaces"
        return redirect("/?create_pw_error=" + create_pw_error + '&user_name=' + user_name + '&enter_email=' + enter_email)
    
    if confirm_pw != create_pw:
        confirm_pw_error = "Passwords do not match"
        return redirect("/?confirm_pw_error=" + confirm_pw_error + '&user_name=' + user_name + '&enter_email=' + enter_email)
    
    if enter_email != '':

        if len(email_segments[0]) > 20 or len(email_segments[0]) < 3:
            enter_email_error = "email name must be between 3 and 20 characters"
            return redirect("/?enter_email_error=" + enter_email_error + '&user_name=' + user_name + '&enter_email=' + enter_email)
    
        if ' ' in enter_email:
            enter_email_error = 'Invalid email address. Cannot contain spaces'
            return redirect("/?enter_email_error=" + enter_email_error + '&user_name=' + user_name + '&enter_email=' + enter_email)

        if '@' not in enter_email or '.' not in enter_email:
            enter_email_error = 'Invalid email address. Should contain exactly 1 "@" and 1 "."'
            return redirect("/?enter_email_error=" + enter_email_error + '&user_name=' + user_name + '&enter_email=' + enter_email)

        if '@' in email_segments[1] or '.' in email_dots[1] or '@' not in enter_email or '.' not in enter_email:
            enter_email_error = 'Invalid email address. Should contain exactly 1 "@" and 1 "."'
            return redirect("/?enter_email_error=" + enter_email_error + '&user_name=' + user_name + '&enter_email=' + enter_email)
    
    user_name_escaped = cgi.escape(user_name, quote=True)
    return render_template('welcome.html', user_name=user_name_escaped)

@app.route("/")
def index():
    user_name_error = request.args.get('user_name_error')
    create_pw_error = request.args.get('create_pw_error')
    confirm_pw_error = request.args.get('confirm_pw_error')
    enter_email_error = request.args.get('enter_email_error')
    user_name = request.args.get('user_name')
    if not user_name:
        user_name = ''
    enter_email = request.args.get('enter_email')
    if not enter_email:
        enter_email = ''
    
    return render_template('edit.html', user_name_error=user_name_error, 
     create_pw_error=create_pw_error, confirm_pw_error=confirm_pw_error, enter_email_error=enter_email_error, user_name=user_name, enter_email=enter_email)

app.run()