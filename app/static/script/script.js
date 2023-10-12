var inputElement = document.getElementById("inputNumeric");
inputElement.addEventListener("focus", function() {
  inputElement.classList.remove("error");
});

async function addClick() {
var inputElement = document.getElementById("inputNumeric");
var value = Number(inputElement.value);
var outputElement = document.getElementById("output");
try {validateInput(value);}
catch(error) {
inputElement.classList.add('error');
outputElement.innerHTML = error;
return
}
var data = {"questions_num": value};
var response = await fetch('/api/v1/questions', {
    method: "POST",
    body: JSON.stringify(data),
    headers: {
      'Content-Type': 'application/json'
    }
  });
if (response.status === 200) {
var questions = await response.json();
if (questions.length > 0) {
outputElement.innerHTML = '';
questions.forEach(function (question) {
    var questionElement = document.createElement("div");
    questionElement.classList.add("elemDiv");
    questionElement.innerHTML = '<b>ID:</b> ' + question.id + '<br><b>Q:</b> ' + question.question + '<br><b>A:</b> ' + question.answer + '<br><b>created:</b> ' + formatDate(question.created_at);
    outputElement.appendChild(questionElement);
  });
}
} else {
console.log('error');
}
}

function formatDate(data) {
	var date = new Date(data);
	var yearUTC = date.getFullYear();
	var monthUTC = date.getMonth() + 1;
	var dayUTC = date.getDate();
	var hoursUTC = date.getHours();
	var minutesUTC = date.getMinutes();
	var secondsUTC = date.getSeconds();
	return `${dayUTC}-${monthUTC}-${yearUTC} ${hoursUTC}:${minutesUTC}:${secondsUTC} UTC`;
}

function validateInput(value) {
if (value < 1 || value > 100) {
throw new Error("Input value should be less than 101 and greater than 0");
}
}