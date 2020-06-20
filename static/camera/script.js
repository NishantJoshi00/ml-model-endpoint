// Constraints for video stream
let constraints = {
	video: {
		facingMode: "user"
	},
	audio: false
}

const cameraView = document.querySelector("#camera-view")
const cameraOutput = document.querySelector("#camera-output")
const cameraSensor = document.querySelector("#camera-sensor")
const cameraTrigger = document.querySelector("#camera-trigger")

// Accessing The device Camera and stream

function cameraStart() {
	navigator.mediaDevices
		.getUserMedia(constraints)
		.then(function(stream) {
			track = stream.getTracks()[0];
			cameraView.srcObject = stream;
		})
		.catch(function(err) {
			console.log("Something is broken", err);
		});
}

cameraTrigger.onclick = function() {
	cameraSensor.width = cameraView.videoWidth;
	cameraSensor.height = cameraView.videoHeight;
	cameraSensor.getContext("2d").drawImage(cameraView, 0, 0);
	cameraOutput.src = cameraSensor.toDataURL("image/webp");
	cameraOutput.classList.add("taken");
}

window.addEventListener("load", cameraStart, false);