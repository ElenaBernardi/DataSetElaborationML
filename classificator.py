import db_queries
import numpy

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

    print(metrics.classification_report(y_test, y_predicted, target_names=['range 0-30', 'range 30-50','range 50-60','range 60-90']))

def prepare_input(dataset):
    X=[]
    y=[]
    for row in dataset:
        X.append((float(row[1]),float(row[2])))
        if int(row[2]) <= 30:
            y.append("range 0-30")
        if int(row[2]) > 30 and int(row[2]) <= 50:
            y.append("range 30-50")
        if int(row[2]) > 50 and int(row[2]) <= 60:
            y.append("range 50-60")
        if int(row[2]) > 60:
            y.append("range 60-90")

    return X,y