function OnTensorflowReady(){
	document.getElementById('status2').innerHTML = 'Tensorflow.js is ready.';
  }


  async function tf_predict(){
	 const model = await tf.loadLayersModel('/model/model.json');

	 //画像オブジェクトを生成
	 var width = 64;
	 var height = 48;
	 
	 var canvas=document.getElementById("canvasOutput");
     var context = canvas.getContext("2d");
     var imageData = context.getImageData(0, 0, width, height);
     const example = tf.browser.fromPixels (imageData).reshape([1,48,64,3]);
	 const prediction = model.predict(example);
	 document.getElementById('result').innerHTML =("この画像は「" + prediction.argMax(-1).dataSync() + "」だよ！");
};
/*
const CLASSES = {0:'A', 1:'B', 2:'C'}

//-----------------------
// start button event
//-----------------------

$("#start-button").click(function(){
	loadModel() ;
	startWebcam();
});

//-----------------------
// load model
//-----------------------

let model;
async function loadModel() {
	console.log("model loading..");
	$("#console").html(`<li>model loading...</li>`);
	model=await tf.loadModel('/model/modej.json');
	console.log("model loaded.");
	$("#console").html(`<li>VGG16 pre trained model loaded.</li>`);
};

//-----------------------
// predict button event
//-----------------------

$("#predict-button").click(function(){
	setInterval(predict, 1000/10);
});

//-----------------------
// TensorFlow.js method
// predict tensor
//-----------------------

async function predict(){
	let tensor = captureWebcam();

	let prediction = await model.predict(tensor).data();
	let results = Array.from(prediction)
				.map(function(p,i){
	return {
		probability: p,
		className: CLASSES[i]
	};
	}).sort(function(a,b){
		return b.probability-a.probability;
	}).slice(0,5);

	$("#console").empty();

	results.forEach(function(p){
		$("#console").append(`<li>${p.className} : ${p.probability.toFixed(6)}</li>`);
		console.log(p.className,p.probability.toFixed(6))
	});

};

//------------------------------
// capture streaming video 
// to a canvas object
//------------------------------

function captureWebcam() {
	var canvas    = document.getElementById("canvasOutput");
	
	tensor_image = preprocessImage(canvas);

	return tensor_image;
}

//-----------------------
// TensorFlow.js method
// image to tensor
//-----------------------

function preprocessImage(image){
	let tensor = tf.fromPixels(image).resizeNearestNeighbor([64,48]).toFloat();	
	let offset = tf.scalar(255);
    return tensor.div(offset).expandDims();
}

//-----------------------
// clear button event
//-----------------------

$("#clear-button").click(function clear() {
	location.reload();
});
*/