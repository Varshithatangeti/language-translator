from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def PN2k23():
    return render_template('PN2k23.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/translatepage')
def translatepage():
    return render_template('translatepage.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Here, you can perform authentication and validation logic.
        # For simplicity, we'll just print the received data.
        print(f'Username: {username}, Password: {password}')
        
        # You can insert data into MongoDB here
        user_data = {
            "username": username,
            "password": password
        }
    
        # You can redirect to a different page after successful login.
       
        return redirect(url_for('translatepage'))
    
    return render_template('login.html')


if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0')