from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

class TraitModel:
    def __init__(self):
        self.features = None
        self.labels = None
        self.clfs = []

    def loadDataToModel(self,x,y):
        self.features =x
        self.labels = y
    def test_train_split(self,percentage,features,labels):
        # split the dataset randomly for a given percentage
        X_train, X_test, y_train, y_test = train_test_split(features,
                                                            labels,
                                                            test_size=percentage,
                                                            random_state=None)
        return X_train,X_test,y_train,y_test


    def randomForest(self,vectorizedSentences,labels):
        #train one classifier
        clf = RandomForestClassifier(n_estimators=100,
                                     criterion='gini',
                                     random_state=None)
        clf.fit(vectorizedSentences, labels)
        return clf

    def train_Classifiers(self,seqfeatures, targets):
        # train all 5 classifiers for 5 Big-O
        for labels in targets:
            clf = self.randomForest(seqfeatures,labels)
            self.clfs.append(clf)

    def test_classifiers(self,seqfeatures, targets,clf):
        y_pred = clf.predict(seqfeatures)
        counter = 0
        # test one classifier accuracy
        for i in range(len(y_pred)):
            if (y_pred[i] == targets[i]):
                counter += 1
        # evaluate the accuracy
        print(f" Accuracy: {counter / len(targets) * 100}")

    def testAllClassifiers(self,text,labels):
        counter =0
        for clf in self.clfs:
            self.test_classifiers(text,labels[counter],clf)
            counter+= 1





