import db_queries
import numpy
import pickle

from sklearn import linear_model
from sklearn import model_selection
from sklearn import metrics

def training(type1,type2):
    trainingset = db_queries.pull_2types_and_age(type1,type2)
    X, y = prepare_input(trainingset)
    # Split the data and the targets into training/testing sets
    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.1, random_state=0)
    regr = linear_model.LogisticRegression(class_weight='balanced')
    X_train = numpy.array(X_train,dtype=numpy.float64)
    regr.fit(X_train, y_train)
    y_predicted = regr.predict(X_test)

    cm = metrics.confusion_matrix(y_test, y_predicted)

    print(metrics.classification_report(y_test, y_predicted, target_names=['range 0-30', 'range 30-40','range 40-60','range 60-90']))

    """saving model"""
    filename = 'finalized_model.sav'

    pickle.dump(regr, open(filename, 'wb'))


def prepare_input(dataset):
    X=[]
    y=[]
    for row in dataset:
        X.append((float(row[1]),float(row[2])))
        if int(row[2]) <= 30:
            y.append("range 0-30")
        if int(row[2]) > 30 and int(row[2]) <= 40:
            y.append("range 30-40")
        if int(row[2]) > 40 and int(row[2]) <= 60:
            y.append("range 40-60")
        if int(row[2]) > 60:
            y.append("range 60-90")

    return X,y

def predict_result(user, type1=5, type2=2):
  file = open('finalized_model.sav', 'rb')
  input = db_queries.pull_avg_value_from_user(user, type1, type2)
  loaded_model = pickle.load(file)
  result = loaded_model.predict(input)
  values = ideal_value_by_range_age(result)
  return result, values

def ideal_value_by_range_age(range):
    values=""
    if range == "range 0-30":
        values = "ideal pulse wave velocity = 90"+"\n"+"ideal weight = 70"+"\n"
    if range == "range 30-40":
        values = "ideal pulse wave velocity = 60" + "\n" + "ideal weight = 60" + "\n"
    if range == "range 40-60":
        values = "ideal pulse wave velocity = 120" + "\n" + "ideal weight = 80" + "\n"
    if range == "range 60-90":
        values = "ideal pulse wave velocity = 50" + "\n" + "ideal weight = 90" + "\n"

    print (values)
    return values