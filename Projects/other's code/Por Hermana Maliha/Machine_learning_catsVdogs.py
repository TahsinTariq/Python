import os
import cv2
import joblib as joblib

feature_det = cv2.xfeatures2d.SIFT_create()
descr_ext = cv2.DescriptorExtractor_create("SIFT")


def getImageMetadata(folderPath):
    training_names = os.listdir(folderPath)
    image_paths = []
    image_classes = []
    class_id = 0
    for training_name in training_names:
        dir = os.path.join(folderPath, training_name)
        class_path = [os.path.join(dir, f) for f in os.listdir(dir)]
        image_paths += class_path
        image_classes += [class_id] * len(class_path)
        class_id += 1
    return image_paths, image_classes


def preProcessImages(image_paths):
    descriptors = []
    for image_path in image_paths:
        im = cv2.imread(image_path)
        kpts = feature_det.detect(im)
        kpts, des = descr_ext.compute(im, kpts)
        descriptors.append(des)
    return descriptors


def train(descriptors, image_classes, image_paths):
    flann_params = dict(algorithm=1, trees=5)
    matcher = cv2.FlannBasedMatcher(flann_params, {})
    bow_extract = cv2.BOWImgDescriptorExtractor(descr_ext, matcher)
    bow_train = cv2.BOWKMeansTrainer(20)
    for des in descriptors:
        bow_train.add(des)
    voc = bow_train.cluster()
    bow_extract.setVocabulary(voc)
    traindata = []
    for imagepath in image_paths:
        featureset = getImagedata(feature_det, bow_extract, imagepath)
        traindata.extend(featureset)
    clf = LinearSVC()
    clf.fit(traindata, np.array(image_classes))
    joblib.dump((voc, clf), "imagereco.pkl", compress=3)


def getImagedata(feature_det, bow_extract, path):
    im = cv2.imread(path)
    featureset = bow_extract.compute(im, feature_det.detect(im))
    return featureset


voc, clf = joblib.load("imagereco.pkl")


def predict(voc, clf):
    flann_params = dict(algorithm=1, trees=5)
    matcher = cv2.FlannBasedMatcher(flann_params, {})
    bow_extract = cv2.BOWImgDescriptorExtractor(descr_ext, matcher)
    bow_extract.setVocabulary(voc)
    testImageFolder = "../../../data/images/testimage/"
    testing_classes = os.listdir(testImageFolder)
    imgPath = []
    type = []
    for foldername in testing_classes:
        dir = os.path.join(testImageFolder, foldername)
        for root, dirs, files in os.walk(dir):
            for file in files:
                imgPath.append(dir + "/" + file)
                featureset = getImagedata(feature_det, bow_extract, dir + "/" + file)
                prediction = clf.predict(featureset)
                if prediction == 1:
                    predictText = "DOG"
                elif prediction == 0:
                    predictText = "CAT"
                type.append(predictText)
