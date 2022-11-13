import pickle
import json
import pandas as pd
import numpy as np
import config


class BreastCancer():
    def __init__(self,mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness,mean_compactness,
    mean_concavity,mean_concave_points,mean_symmetry,mean_fractal_dimension,radius_error,texture_error,
    perimeter_error,area_error,smoothness_error,compactness_error,concavity_error,concave_points_error,
    symmetry_error,fractal_dimension_error,worst_radius,worst_texture,worst_perimeter,worst_area,
    worst_smoothness,worst_compactness,worst_concavity,worst_concave_points,worst_symmetry,
    worst_fractal_dimension):
        self.mean_radius = mean_radius
        self.mean_texture = mean_texture
        self.mean_perimeter = mean_perimeter
        self.mean_area = mean_area
        self.mean_smoothness = mean_smoothness
        self.mean_compactness = mean_compactness
        self.mean_concavity = mean_concavity
        self.mean_concave_points = mean_concave_points
        self.mean_symmetry = mean_symmetry
        self.mean_fractal_dimension = mean_fractal_dimension
        self.radius_error = radius_error
        self.texture_error = texture_error
        self.perimeter_error = perimeter_error
        self.area_error = area_error
        self.smoothness_error = smoothness_error
        self.compactness_error = compactness_error
        self.concavity_error = concavity_error
        self.mean_concave_points_error = concave_points_error
        self.symmetry_error = symmetry_error
        self.fractal_dimension_error = fractal_dimension_error
        self.worst_radius = worst_radius
        self.worst_texture = worst_texture
        self.worst_perimeter = worst_perimeter
        self.worst_area = worst_area
        self.worst_smoothness = worst_smoothness
        self.worst_compactness = worst_compactness
        self.worst_concavity = worst_concavity
        self.worst_concave_points = worst_concave_points
        self.worst_symmetry = worst_symmetry
        self.worst_fractal_dimension = worst_fractal_dimension

    def load_file(self):
        with open(config.MODEL_FILE_PATH, "rb") as f:
            self.breast_model = pickle.load(f)

        with open(config.JSON_FILE_PATH, "r") as f:
            self.json_data = json.load(f)


    def get_predicted_symptoms_cancer(self):
        self.load_file()  # calling load_file method to get

        array = np.zeros(len(self.json_data['columns']))

        array[0] = self.mean_radius
        array[1] = self.mean_texture
        array[2] = self.mean_perimeter
        array[3] = self.mean_area
        array[4] = self.mean_smoothness
        array[5] = self.mean_compactness
        array[6] = self.mean_concavity
        array[7] = self.mean_concave_points
        array[8] = self.mean_symmetry
        array[9] = self.mean_fractal_dimension
        array[10] = self.radius_error
        array[11] = self.texture_error
        array[12] = self.perimeter_error
        array[13] = self.area_error
        array[14] = self.smoothness_error
        array[15] = self.compactness_error
        array[16] = self.concavity_error
        array[17] = self.mean_concave_points_error
        array[18] = self.symmetry_error
        array[19] = self.fractal_dimension_error
        array[20] = self.worst_radius
        array[21] = self.worst_texture
        array[22] = self.worst_perimeter
        array[23] = self.worst_area
        array[24] = self.worst_smoothness
        array[25] = self.worst_compactness
        array[26] = self.worst_concavity
        array[27] = self.worst_concave_points
        array[28] = self.worst_symmetry
        array[29] = self.worst_fractal_dimension

        print("Test Array -->\n",array)
        predicted_cancer = self.breast_model.predict([array])[0]
        return predicted_cancer





if __name__ == "__main__":

    mean_radius = 17.99
    mean_texture = 10.38
    mean_perimeter = 122.80
    mean_area = 1000
    mean_smoothness = 0.118
    mean_compactness = 0.277
    mean_concavity = 0.300
    mean_concave_points = 0.147
    mean_symmetry = 0.241
    mean_fractal_dimension = 0.152
    radius_error = 1.095
    texture_error = 0.905
    perimeter_error = 8.58
    area_error = 153
    smoothness_error = 0.006
    compactness_error = 0.049
    concavity_error = 0.053
    concave_points_error = 0.01
    symmetry_error = 0.030030
    fractal_dimension_error = 0.02
    worst_radius = 25.38
    worst_texture = 17.33
    worst_perimeter = 184
    worst_area = 2019
    worst_smoothness = 0.162
    worst_compactness = 0.665
    worst_concavity = 0.711
    worst_concave_points = 0.265
    worst_symmetry = 0.460
    worst_fractal_dimension = 0.118

    bc = BreastCancer(mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness,mean_compactness,
    mean_concavity,mean_concave_points,mean_symmetry,mean_fractal_dimension,radius_error,texture_error,
    perimeter_error,area_error,smoothness_error,compactness_error,concavity_error,concave_points_error,
    symmetry_error,fractal_dimension_error,worst_radius,worst_texture,worst_perimeter,worst_area,
    worst_smoothness,worst_compactness,worst_concavity,worst_concave_points,worst_symmetry,
    worst_fractal_dimension)
    cancer = bc.get_predicted_symptoms_cancer()
    print()
    print(f"predicted diabetes disease patients {cancer}")
    # if disease == 1:
    #     print('yes patient has a heart disease')
    # else:
    #     print('patient has not a heart disease')

