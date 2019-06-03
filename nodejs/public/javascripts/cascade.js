let imgElement = document.getElementById('imageSrc');
let inputElement = document.getElementById('fileInput');
inputElement.addEventListener('change', (e) => {
  imgElement.src = URL.createObjectURL(e.target.files[0]);
  }, false);


  imgElement.onload = function(){
    let src = cv.imread(imgElement);
    let gray = new cv.Mat();
    cv.cvtColor(src, gray, cv.COLOR_RGBA2GRAY, 0);
    let faces = new cv.RectVector();
    let utils = new Utils('errorMessage'); //use utils class
    let faceCascadeFile = 'cascade/haarcascade_frontalface_default.xml'; // path to xml
    let faceCascade = new cv.CascadeClassifier();
    // load pre-trained classifiers
    // use createFileFromUrl to "pre-build" the xml
    utils.createFileFromUrl(faceCascadeFile, faceCascadeFile, () => {
      faceCascade.load(faceCascadeFile); // in the callback, load the cascade from file 
    });
    // detect faces
    let msize = new cv.Size(0, 0);
    faceCascade.detectMultiScale(gray, faces, 1.1, 3, 0, msize, msize);
    for (let i = 0; i < faces.size(); ++i) {
        let roiGray = gray.roi(faces.get(i));
        let roiSrc = src.roi(faces.get(i));
        let point1 = new cv.Point(faces.get(i).x, faces.get(i).y);
        let point2 = new cv.Point(faces.get(i).x + faces.get(i).width,
                                  faces.get(i).y + faces.get(i).height);
        cv.rectangle(src, point1, point2, [255, 0, 0, 255]);
        // detect eyes in face ROI
        
        roiGray.delete(); roiSrc.delete();
    }
    cv.imshow('canvasOutput', src);
    src.delete(); gray.delete(); faceCascade.delete(); faces.delete();
    }

    function onOpenCvReady() {
        document.getElementById('status1').innerHTML = 'OpenCV.js is ready.';
      }