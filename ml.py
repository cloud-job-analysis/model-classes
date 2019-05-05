import time
from sklearn.datasets import load_iris
from sklearn.datasets import load_digits
from sklearn.datasets import load_wine
from sklearn.datasets import load_breast_cancer
from sklearn.svm import SVC
import argparse

parser = argparse.ArgumentParser(description='Get training data')

parser.add_argument('--dataset', help='dataset name')

args = parser.parse_args()

dataset = args.dataset

def load_data(dataset):
	if dataset == 'iris':
		return load_iris(return_X_y=True)
	elif dataset == 'mnist':
		return load_digits(return_X_y=True)
	elif dataset == 'wine':
		return load_wine(return_X_y=True)
	elif dataset == 'cancer':
		return load_breast_cancer(return_X_y=True)
	else:
		raise ValueError

X, y  = load_data(args.dataset)
print(X.shape)
print(y.shape)
clf = SVC()
clf.fit(X, y)
