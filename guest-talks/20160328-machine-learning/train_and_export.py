#!/usr/bin/python

import httplib
import json

from mnist import MNIST
import numpy as np
import pandas
import sklearn_pandas
from sklearn import neural_network as nn
from sklearn.preprocessing import StandardScaler
from sklearn2pmml import sklearn2pmml


def query_digit(digit):
    host, port = "localhost", 4567
    con = httplib.HTTPConnection(host, port)
    params = json.dumps({"data": digit})
    con.request("POST", "/digit", params)
    response = con.getresponse()
    print "For digit:%s\nReceived prediction response [%s]\n" % (MNIST.display(digit), response.read())


def draw_random_misclassification(truth_array, prediction, test_label, test_data):
    """
    Prints the prediction, label and digit for a random misclassified sample
    """
    incorrect_idx = [idx for idx, is_true in enumerate(truth_array) if not is_true]
    n = incorrect_idx[np.random.randint(0, len(incorrect_idx))]
    print "predicted [%s]\nlabeled [%s]\nraw data:\n%s" % (prediction[n].argmax(), test_label[n], MNIST.display(test_data[n]))


def main():
    data = MNIST('./data')
    col_names = ["x" + str(x) for x in range(784)]
    # Define a transform function that will be serialized with the model
    mnist_mapper = sklearn_pandas.DataFrameMapper([(col_names, StandardScaler()), ("digit", None)])

    # 60,000 train samples of 28x28 grid, domain 0-255
    mnist_train_data, mnist_train_label = data.load_training()
    mnist_train_df = pandas.concat((pandas.DataFrame(mnist_train_data, columns=col_names),
                                    pandas.DataFrame(list(mnist_train_label), columns=["digit"])),
                                   axis=1)
    mnist_train_df_norm = mnist_mapper.fit_transform(mnist_train_df)

    mlp_config = {'hidden_layer_sizes': (1000,),
                  'activation': 'tanh',
                  'algorithm': 'adam',
                  'max_iter': 20,
                  'early_stopping': True,
                  'validation_fraction': 0.1,
                  'verbose': True
                  }
    mnist_classifier = nn.MLPClassifier(**mlp_config)
    mnist_classifier.fit(X=mnist_train_df_norm[:, 0:28 * 28], y=mnist_train_df_norm[:, 28 * 28])

    # 10,000 test samples
    mnist_test_data, mnist_test_label = data.load_testing()
    mnist_test_df = pandas.concat((pandas.DataFrame(mnist_test_data, columns=col_names),
                                   pandas.DataFrame(list(mnist_test_label), columns=["digit"])),
                                  axis=1)
    mnist_test_df_norm = mnist_mapper.fit_transform(mnist_test_df)

    prediction = mnist_classifier.predict_proba(mnist_test_df_norm[:, 0:28 * 28])
    truth_array = [prediction[idx].argmax() == mnist_test_label[idx] for idx in range(len(prediction))]
    accuracy = float(sum(truth_array)) / float(len(truth_array))
    print "out of sample model accuracy [%s]" % accuracy
    print "serializing to pmml"
    sklearn2pmml(mnist_classifier, mnist_mapper, "MLP_MNIST.pmml", with_repr=True)

if __name__ == '__main__':
    main()
