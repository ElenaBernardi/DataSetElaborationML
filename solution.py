import clustering
import plot2D
from sklearn import linear_model
from sklearn.cross_decomposition import tests


def create_model(type1,type2):
    dataset = plot2D.fromArray_toVectorTuples(type1,type2)
    # Restituisce tuple di tipo Numpy arrays: (x_train, y_train), (x_test, y_test)
    (train_data, train_labels), (test_data, test_labels) = dataset.load_data()

