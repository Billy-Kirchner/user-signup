from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/welcome", methods=['POST'])
def welcome():
    user_name = request.form['user-name']
    if len(user_name) > 20 or len(user_name) < 3:
        user_name_error = "Username must be between 3 and 20 characters"
        return redirect("/?user_name_error =" + user_name_error)

    user_name_escaped = cgi.escape(user_name, quote=True)
    return render_template('welcome.html', user_name=user_name)

@app.route("/")
def index():
    user_name_error = request.args.get('user_name_error')
    create_pw_error = request.args.get('create_pw_error')
    confirm_pw_error = request.args.get('confirm_pw_error')
    enter_email_error = request.args.get('enter_email_error')

    if not user_name_error:
        user_name_error = ''
    if not create_pw_error:
        create_pw_error = ''
    if not confirm_pw_error:
        confirm_pw_error = ''
    if not enter_email_error:
        enter_email_error = ''
    
    return render_template('edit.html', user_name_error=user_name_error and cgi.escape(user_name_error, quote=True), 
     create_pw_error=create_pw_error, confirm_pw_error=confirm_pw_error, enter_email_error=enter_email_error)

app.run()