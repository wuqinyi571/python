from sklearn import svm
from sklearn import datasets

digits = datasets.load_digits()

print (digits.data)
print (digits.target)
clf = svm.SVC(gamma=0.0001, C=100)
clf.fit(digits.data[:-1], digits.target[:-1])
result = clf.predict(digits.data[1])