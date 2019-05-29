const cv = require('opencv4nodejs');
const input  = __dirname+'/../images/lenna.jpg';
const output = __dirname+'/../images/output.jpg';
console.log(input);
var src = cv.imread(input).bgrToGray();
var img = src.resize(100,100);
cv.imwrite(output, img);
/*
const matRGBA = img.channels === 1
  ? img.cvtColor(cv.COLOR_GRAY2RGBA)
  : img.cvtColor(cv.COLOR_BGR2RGBA);

const imgData = new cv.Mat(
  new Uint8ClampedArray(matRGBA.getData()),
  img.cols,
  img.rows
);

const canvas = document.getElementById('myCanvas');
canvas.height = img.rows;
canvas.width = img.cols;

// set image data
const ctx = canvas.getContext('2d');
ctx.drowimage(imgData, 0, 0);
*/
/*

let src = cv.imread('canvasInput');
let dst = new cv.Mat();
let dsize = new cv.Size(300, 300);
// You can try more different parameters
cv.resize(src, dst, dsize, 0, 0, cv.INTER_AREA);
cv.imshow('canvasOutput', dst);
src.delete(); dst.delete();

////////
const img = cv.imread('./lenna.jpg');

const classifier = new cv.CascadeClassifier(cv.HAAR_FRONTALFACE_ALT2);

const grayImg = img.bgrToGray();

const result = classifier.detectMultiScale(grayImg);

if (!result.objects.length) {
  throw new Error('failed to detect faces');
}

const minDetections = 10;
result.objects.forEach((faceRect, i) => {
  if (result.numDetections[i] < minDetections) {
    return;
  }
  const rect = cv.drawDetection(
    img,
    faceRect,
    { color: new cv.Vec(255, 0, 0), segmentFraction: 4 }
  );
});
cv.imshowWait('result', img);
*/
