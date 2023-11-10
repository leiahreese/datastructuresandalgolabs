from flask import Flask, render_template, request
import math

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works', methods=['GET', 'POST'])
def works():
    return render_template("works.html")

@app.route('/templates/area_of_triangle.html', methods=['GET', 'POST'])
def area_of_triangle():
    result = None
    if request.method == 'POST':
        base = float(request.form.get('base', 0))
        height = float(request.form.get('height', 0))
        result = 0.5 * base * height
        return render_template('area_of_triangle.html', result=result)

    return render_template('area_of_triangle.html', result=result)

@app.route('/templates/touppercase.html', methods=['GET', 'POST'])
def to_uppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
        return render_template('touppercase.html', result=result)

    return render_template('touppercase.html')

@app.route('/templates/areaOfcircle.html', methods=['GET', 'POST'])
def area_of_circle():
    result = None
    if request.method == 'POST':
        radius = float(request.form.get('radius', 0))
        result = math.pi * (radius ** 2)
        return render_template('areaOfcircle.html', radius=radius, result=result)

    return render_template('areaOfcircle.html', result=result)


@app.route('/contact')
def contact():
     return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
