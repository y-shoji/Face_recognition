function OnTensorflowReady(){
	document.getElementById('status2').innerHTML = 'Tensorflow.js is ready.';
  }

	const CLASSES = {0:'A', 1:'B', 2:'C'};
  async function tf_predict(){
	 const model = await tf.loadLayersModel('/model/model.json');

	 //画像オブジェクトを生成
		var width = 64;
		var height = 48;
	 
		var canvas=document.getElementById("canvasOutput");
    var context = canvas.getContext("2d");
    var imageData = context.getImageData(0, 0, width, height);
		const tensor_img = tf.browser.fromPixels (imageData).reshape([1,48,64,3]);
		var offset = tf.scalar(255);
		pre_img=tensor_img.div(offset);
		const prediction = model.predict(pre_img);
		const logits = Array.from(prediction.dataSync());
		document.getElementById('result1').innerHTML =("この写真は"+CLASSES[prediction.argMax(-1).dataSync()]+"です。");
		document.getElementById('result2').innerHTML =(CLASSES[0]+":"+logits[0].toFixed(4)*100+"%<br>"+
																				 CLASSES[1]+":"+logits[1].toFixed(4)*100+"%<br>"+
																				 CLASSES[2]+":"+logits[2].toFixed(4)*100+"%<br>");
};
