from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/user/<name>') #url that has a variable in it

def greet(name):
    return render_template('greet.html', name=name)

def readDetails(filename):
    with open(filename, 'r') as f: #opens the file in read mode
        return [line for line in f]
    
def writeToFile(filename, message):
    with open(filename, 'a') as f:  # opens file in append mode adding to the end of it
        f.write(message)

@app.route("/")
def homeInfo():
    name = "Pepe Duran"          # declare variables
    aboutMe = readDetails('static/details.txt')    # pass them in as arguments (could be title = title)
    return render_template("base01.html", name = name, aboutMe = aboutMe) # varaibles to use in the html

#code for a /form page that takes input and routes user to another page
@app.route('/form', methods=['GET', 'POST'])
def formDemo():
    name = None # name is nothing  but we need a variable name to pass in render_template call
    if request.method == 'POST':
        if request.form['name']:
            name = request.form['name']
            writeToFile('/static/comments.txt', name)
            # return render_template('greet.html', name=name)

    return render_template('form.html', name=name)

if __name__ == "__main__":
    app.run(debug = True, port = 3000) 