from flask import Flask, render_template, request
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
from models import *

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def prediction():

    xTrain = pd.read_csv('./data/rawxTrain.csv')
    # scaler = StandardScaler()
    # scaler.fit(xTrain)

    #LIST
    data_input = []

    cap_diameter = float(request.form['cap'])
    data_input.append(cap_diameter)

    Bruises = np.zeros(1)
    Bruise = int(request.form.get("Bruise"))
    # Bruises = scaler.transform(Bruises)
    data_input.append(Bruise)

    stem_height = float(request.form['stem-height'])
    data_input.append(stem_height)

    vail_type = 1
    vail_type = vail_type
    data_input.append(vail_type)

    Has_ring = int(request.form['has_ring'])
    data_input.append(Has_ring)

    shapes = np.zeros(6)
    shape = int(request.form['shape'])
    shapes[shape] = 1
    for i in shapes:
        data_input.append(i)

    caps_surface = np.zeros(9)
    cap_surface = int(request.form['cap-surface'])
    caps_surface[cap_surface] = 1
    for i in caps_surface:
        data_input.append(i)

    caps_color = np.zeros(11)
    cap_color = int(request.form['cap-color'])
    caps_color[cap_color] = 1
    for i in caps_color:
        data_input.append(i)

    gills_attachment = np.zeros(7)
    gill_attachment = int(request.form['gill-attachment'])
    gills_attachment[gill_attachment] = 1
    for i in gills_attachment:
        data_input.append(i)

    gill_spacing = int(request.form['gill-spacing'])
    data_input.append(gill_spacing)

    gills_color = np.zeros(12)
    gill_color = int(request.form['gill-color'])
    gills_color[gill_color] = 1
    for i in gills_color:
        data_input.append(i)

    stems_root = np.zeros(6)
    stem_root = int(request.form['stem-root'])
    stems_root[stem_root] = 1
    for i in stems_root:
        data_input.append(i)

    stems_surface = np.zeros(10)
    stem_surface = int(request.form['stem-surface'])
    stems_surface[stem_surface] = 1
    for i in stems_surface:
        data_input.append(i)

    stems_color = np.zeros(10)
    stem_color = int(request.form['stem-color'])
    stems_color[stem_color] = 1
    for i in stems_color:
        data_input.append(i)

    veils_color = np.zeros(11)
    veil_color = int(request.form['veil-color'])
    veils_color[veil_color] = 1
    for i in veils_color:
        data_input.append(i)

    rings = np.zeros(10)
    ring = int(request.form['ring'])
    rings[ring] = 1
    for i in rings:
        data_input.append(i)

    spores = np.zeros(11)
    spore = int(request.form['spore-print-color'])
    spores[spore] = 1
    for i in spores:
        data_input.append(i)

    habitats = np.zeros(7)
    habitat = int(request.form['habitat'])
    habitats[habitat] = 1
    for i in habitats:
        data_input.append(i)

    seasons = np.zeros(2)
    season = int(request.form['season'])
    seasons[season] = 1
    for i in seasons:
        data_input.append(i)
    #LIST -> NP ARRAY
    array = np.array(data_input)
    knn_prediction_class = knn_prediction(array)
    dt_prediction_class = dt_prediction(array)
    NB_class = NB_prediction(array)
    LGISTC_class = Logistic_Regression_prediction(array)
    RM_Forest = Random_Forest_prediction(array)
    # SVMach = SVMachines(array)

    return render_template("table.html", knn=knn_prediction_class, dt=dt_prediction_class,
                           RM_Forest=RM_Forest, LGISTC=LGISTC_class, NB=NB_class)
    # dt=dt_prediction_class, SVMach=SVMach,
    #                        RM_Forest=RM_Forest, NB=NB_class, LGISTC=LGISTC_class


if __name__ == "__main__":
    app.run(debug=True)
