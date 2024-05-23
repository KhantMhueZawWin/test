import pandas as pd 
from sklearn.model_selection import train_test_split
from data import data
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

def data():
  df=pd.read_csv("iris_orig.csv")
  X= df.drop('species', axis=1)
  y=df['species']
  X=StandardScaler().fit_transform(X)
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
  return X_train, X_test, y_train, y_test
def DecisionT(X_train, X_test, y_train, y_test):
  DT=DecisionTreeClassifier()
  DT.fit(X_train, y_train)
  y_pred = DT.predict(X_test)
  accuracy = accuracy_score(y_test, y_pred)*100
def RandomF(X_train, X_test, y_train, y_test):


def main():
if __name__ == "__main__":
  main()