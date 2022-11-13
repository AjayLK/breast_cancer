

from flask import Flask, jsonify, render_template, request
from breast_model.utils import BreastCancer
import config

app = Flask(__name__)

@app.route('/')
def hello_flask():
    print("Welcome")
    return render_template("index.html")

@app.route('/predicted_cancer',methods = ['GET','POST'])
def get_cancer_disease():
    if request.method == 'GET':
        print('we are using Get method')
    
        data = request.form
        print("Data-->",data)

        mean_radius = eval(request.args.get('mean_radius'))
        mean_texture = eval(request.args.get('mean_texture'))
        mean_perimeter = eval(request.args.get('mean_perimeter'))
        mean_area = eval(request.args.get('mean_area'))
        mean_smoothness = eval(request.args.get('mean_smoothness'))
        mean_compactness = eval(request.args.get('mean_compactness'))
        mean_concavity = eval(request.args.get('mean_concavity'))
        mean_concave_points = eval(request.args.get('mean_concave_points'))
        mean_symmetry = eval(request.args.get('mean_symmetry'))
        mean_fractal_dimension = eval(request.args.get('mean_fractal_dimension'))
        radius_error = eval(request.args.get('radius_error'))
        texture_error = eval(request.args.get('texture_error'))
        perimeter_error = eval(request.args.get('perimeter_error'))
        area_error = eval(request.args.get('area_error'))
        smoothness_error = eval(request.args.get('smoothness_error'))
        compactness_error = eval(request.args.get('compactness_error'))
        concavity_error = eval(request.args.get('concavity_error'))
        concave_points_error = eval(request.args.get('concave_points_error'))
        symmetry_error = eval(request.args.get('symmetry_error'))
        fractal_dimension_error = eval(request.args.get('fractal_dimension_error'))
        worst_radius = eval(request.args.get('worst_radius'))
        worst_texture = eval(request.args.get('worst_texture'))
        worst_perimeter = eval(request.args.get('worst_perimeter'))
        worst_area = eval(request.args.get('worst_area'))
        worst_smoothness = eval(request.args.get('worst_smoothness'))
        worst_compactness = eval(request.args.get('worst_compactness'))
        worst_concavity = eval(request.args.get('worst_concavity'))
        worst_concave_points = eval(request.args.get('worst_concave_points'))
        worst_symmetry = eval(request.args.get('worst_symmetry'))
        worst_fractal_dimension = eval(request.args.get('worst_fractal_dimension'))

        print("""mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness,mean_compactness,
    mean_concavity,mean_concave_points,mean_symmetry,mean_fractal_dimension,radius_error,texture_error,
    perimeter_error,area_error,smoothness_error,compactness_error,concavity_error,concave_points_error,
    symmetry_error,fractal_dimension_error,worst_radius,worst_texture,worst_perimeter,worst_area,
    worst_smoothness,worst_compactness,worst_concavity,worst_concave_points,worst_symmetry,
    worst_fractal_dimension""",mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness,mean_compactness,
    mean_concavity,mean_concave_points,mean_symmetry,mean_fractal_dimension,radius_error,texture_error,
    perimeter_error,area_error,smoothness_error,compactness_error,concavity_error,concave_points_error,
    symmetry_error,fractal_dimension_error,worst_radius,worst_texture,worst_perimeter,worst_area,
    worst_smoothness,worst_compactness,worst_concavity,worst_concave_points,worst_symmetry,
    worst_fractal_dimension)

        bc = BreastCancer(mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness,mean_compactness,
        mean_concavity,mean_concave_points,mean_symmetry,mean_fractal_dimension,radius_error,texture_error,
        perimeter_error,area_error,smoothness_error,compactness_error,concavity_error,concave_points_error,
        symmetry_error,fractal_dimension_error,worst_radius,worst_texture,worst_perimeter,worst_area,
        worst_smoothness,worst_compactness,worst_concavity,worst_concave_points,worst_symmetry,
        worst_fractal_dimension)
        cancer = bc.get_predicted_symptoms_cancer()

        if cancer == 1:
            return render_template("index.html", prediction="She is having breast cancer.")
        else:
            return render_template("index.html", prediction="She doesn't have breast cancer,you should live your next life happily.")


    else: 
        print('we are using Post method')
    
        data = request.form
        print("Data-->",data)

        mean_radius = eval(request.form.get('mean_radius'))
        mean_texture = eval(request.form.get('mean_texture'))
        mean_perimeter = eval(request.form.get('mean_perimeter'))
        mean_area = eval(request.form.get('mean_area'))
        mean_smoothness = eval(request.form.get('mean_smoothness'))
        mean_compactness = eval(request.form.get('mean_compactness'))
        mean_concavity = eval(request.form.get('mean_concavity'))
        mean_concave_points = eval(request.form.get('mean_concave_points'))
        mean_symmetry = eval(request.form.get('mean_symmetry'))
        mean_fractal_dimension = eval(request.form.get('mean_fractal_dimension'))
        radius_error = eval(request.form.get('radius_error'))
        texture_error = eval(request.form.get('texture_error'))
        perimeter_error = eval(request.form.get('perimeter_error'))
        area_error = eval(request.form.get('area_error'))
        smoothness_error = eval(request.form.get('smoothness_error'))
        compactness_error = eval(request.form.get('compactness_error'))
        concavity_error = eval(request.form.get('concavity_error'))
        concave_points_error = eval(request.form.get('concave_points_error'))
        symmetry_error = eval(request.form.get('symmetry_error'))
        fractal_dimension_error = eval(request.form.get('fractal_dimension_error'))
        worst_radius = eval(request.form.get('worst_radius'))
        worst_texture = eval(request.form.get('worst_texture'))
        worst_perimeter = eval(request.form.get('worst_perimeter'))
        worst_area = eval(request.form.get('worst_area'))
        worst_smoothness = eval(request.form.get('worst_smoothness'))
        worst_compactness = eval(request.form.get('worst_compactness'))
        worst_concavity = eval(request.form.get('worst_concavity'))
        worst_concave_points = eval(request.form.get('worst_concave_points'))
        worst_symmetry = eval(request.form.get('worst_symmetry'))
        worst_fractal_dimension = eval(request.form.get('worst_fractal_dimension'))

        print("""mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness,mean_compactness,
        mean_concavity,mean_concave_points,mean_symmetry,mean_fractal_dimension,radius_error,texture_error,
        perimeter_error,area_error,smoothness_error,compactness_error,concavity_error,concave_points_error,
        symmetry_error,fractal_dimension_error,worst_radius,worst_texture,worst_perimeter,worst_area,
        worst_smoothness,worst_compactness,worst_concavity,worst_concave_points,worst_symmetry,
        worst_fractal_dimension""",mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness,mean_compactness,
        mean_concavity,mean_concave_points,mean_symmetry,mean_fractal_dimension,radius_error,texture_error,
        perimeter_error,area_error,smoothness_error,compactness_error,concavity_error,concave_points_error,
        symmetry_error,fractal_dimension_error,worst_radius,worst_texture,worst_perimeter,worst_area,
        worst_smoothness,worst_compactness,worst_concavity,worst_concave_points,worst_symmetry,
        worst_fractal_dimension)

        bc = BreastCancer(mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness,mean_compactness,
        mean_concavity,mean_concave_points,mean_symmetry,mean_fractal_dimension,radius_error,texture_error,
        perimeter_error,area_error,smoothness_error,compactness_error,concavity_error,concave_points_error,
        symmetry_error,fractal_dimension_error,worst_radius,worst_texture,worst_perimeter,worst_area,
        worst_smoothness,worst_compactness,worst_concavity,worst_concave_points,worst_symmetry,
        worst_fractal_dimension)
        cancer = bc.get_predicted_symptoms_cancer()

        if cancer == 1:
            return render_template("index.html", prediction="She is having symptoms of breast cancer.")
        else:
            return render_template("index.html", prediction="She is not having symptoms of breast cancer.")

  

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = config.PORT_NUMBER, debug = True)