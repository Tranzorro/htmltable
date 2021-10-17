from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def default():
    users = [
        {'First_name': 'Michael', 'Last_name': 'Choi'},
        {'First_name': 'John', 'Last_name': 'Supsupin'},
        {'First_name': 'Mark', 'Last_name': 'Guillen'},
        {'First_name': 'KB', 'Last_name': 'Tonel'},
    ]
    return render_template('index.html', userlist = users)

if __name__ == "__main__":
    app.run(debug=True)