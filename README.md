__FACE DETECTION THROUGH HAARCASCADE CLASSIFIER__

OpenCV provides a training method (see Cascade Classifier Training) or pretrained models, that can be read using the cv::CascadeClassifier::load method. The pretrained models are located in the data folder in the OpenCV installation or can be found here.

The following code example will use pretrained Haar cascade models to detect faces and eyes in an image. First, a cv::CascadeClassifier is created and the necessary XML file is loaded using the cv::CascadeClassifier::load method. Afterwards, the detection is done using the cv::CascadeClassifier::detectMultiScale method, which returns boundary rectangles for the detected faces or eyes.


<img width="580" alt="face result" src="https://user-images.githubusercontent.com/72192238/95127894-5fd10000-0776-11eb-8794-fccc87342b26.PNG">
