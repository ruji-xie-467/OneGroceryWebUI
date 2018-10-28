from flask import Flask, render_template, redirect, url_for, request# Route for handling the login page logic


# create the application object
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def pick():
    error = None
    if request.method == 'POST':
        if request.form['phonenumber'] != 'admin' or request.form['zipcode'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
            letsdoit(request.form)
        else:
            return redirect(url_for('pick'))
    return render_template('pick.html', error=error)

def letsdoit(order):
    print order['peach']

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
