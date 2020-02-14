import pandas as pd
glass_data = pd.read_csv('/content/drive/My Drive/Python_Lesson4/Python_Lesson4/glass.csv')
x=glass_data.drop('Type',axis=1)
y=glass_data['Type']
from sklearn import model_selection
X_train, X_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.2,random_state=0)
from sklearn import svm
lc = svm.SVC(kernel="linear")
lc.fit(X_train, y_train)
y_pred = lc.predict(X_test)
from sklearn import metrics
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
print("classification_report\n",metrics.classification_report(y_test,y_pred))
print("confusion matrix\n",metrics.confusion_matrix(y_test,y_pred))