from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def head():
    message = "This is my first conditional experience in Flask :))"
    return render_template("index.html", yasin = message)


@app.route("/for")
def for_example():
    names = ['Yasin', 'John', 'Gerard', 'Fatih', 'Veysel', 'Serdar' ]
    return render_template("second.html", who = names)



if __name__ == '__main__':
    app.run(debug = True)