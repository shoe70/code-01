//
//	site.js
//	landingpager
//
//	Created by Shaunak Ghosh on 10/11/2023.
//

// BUTTON FUNCTIONS
// to use these functions in code:
// <button type="button" onclick="INSERT_FUNCTION_NAME">BUTTON_NAME</button>
// alert the user when pressed.
function button_alert(print) {
	alert(print);
}

// ask the user for an answer, then compare to correct answer
// and reply accordingly
function button_prompt(prompt, answer, response, nullresponse) {
	var question = prompt(prompt);
	if (question == answer) {
		alert(response);
	} else {
		alert(nullresponse);
	}
}

// GETELEMENTBYID FUNCTIONS
// example:
// <p id="para">hello world</p>
// <button type="button" onclick="change_colour(#549d33ce, para)">
// change the specified text to a 
// specified colour

function change_colour(colour, id) {
	const element = document.getElementById(id);
	element.style.color = colour;
}

// change text to a random number
function rand_number(range, id) {
	var random = Math.floor(Math.random() * range);
	let string = random.toString();
	const element = document.getElementById(id);
	element.innerHTML = string;
}

// change text to a new specified string
// recommended max chars = 1000
function change_text(newtext, id) {
	const element = document.getElementById(id);
	element.innerHTML = newtext;
}