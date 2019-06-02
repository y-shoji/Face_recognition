
let imgElement = document.getElementById('imageSrc');
let inputElement = document.getElementById('fileInput');
inputElement.addEventListener('change', (e) => {
  imgElement.src = URL.createObjectURL(e.target.files[0]);
  }, false);

imgElement.onload = function() {
  let input_img = cv.imread(imgElement);
  let resize_img = new cv.Mat();
  let dsize = new cv.Size(64, 48);
  // 100x100にリサイズ
  cv.resize(input_img, resize_img, dsize, 0, 0, cv.INTER_AREA);
  input_img.delete();

  let gray_img = new cv.Mat();
  //グレイスケール化
  cv.cvtColor(resize_img,gray_img, cv.COLOR_RGBA2GRAY, 0);
  cv.imshow('canvasOutput', gray_img);
  resize_img.delete(); gray_img.delete();
};

function onOpenCvReady() {
  document.getElementById('status1').innerHTML = 'OpenCV.js is ready.';
}