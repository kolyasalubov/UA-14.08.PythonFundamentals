from math import pi
from flask import Flask, render_template, url_for, request, flash

app = Flask(__name__)
app.config['SECRET_KEY']="dfslfkjdkfdsfsdfssddffdkjkeig[bv"

areas = ["rectangle", "triangle", "circle"]


@app.route('/')
@app.route('/home')
def main_page():
    return render_template("home.html", areas=areas)


@app.route('/about')
def second_page():
    return render_template("about.html", title="about")


@app.route('/area/<area>', methods=["POST", "GET"])
def area_calc(area):
    try :
        if request.method=="POST":
            if area == "rectangle":
                a= int(request.form['height'])
                b= int(request.form['width'])
                flash(f" Result of {area} : {float(a*b)} cm²")
            elif area == "triangle":
                a= int(request.form['base'])
                b= int(request.form['height'])
                flash(f" Result of {area} : {float((1/3)*a*b)} cm²")
            elif area == "circle":
                a= int(request.form['radius'])
                flash(f" Result of {area} : {round(pi*a**2, 1)} cm²")
    except ValueError as e:
        flash(f" Result of {e}")




    return render_template("area.html", title="Calculator", areas=areas, area=area)


if __name__ == '__main__':
    app.run(debug=True)
