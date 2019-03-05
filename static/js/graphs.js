/*
infoList format:
[cardImage, low, mid, high, market]
*/

function loadGraphs() {
    var cardName = document.getElementById('cardSearch').value;
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState === 4 && this.status === 200) {
        displayContent(this.response);
      }
    };
    xhttp.open("GET", "/card/ " + cardName + "");
    xhttp.send();
}
  
function displayContent(jstring) {
	newString = JSON.parse(jstring);
	//Display bar graph
	var data = [
		{
			x: ['Low', 'Mid', 'High', 'Market'],
			y: [newString[1], newString[2], newString[3], newString[4]],
			type: 'bar',
			name: 'Normal Prices'
		}
	];
	Plotly.newPlot('barGraph', data);
	//Display table
	var values = [
		[newString[4]],
		[newString[1]],
		[newString[2]],
		[newString[3]]
	]
	var data = [{
			type: 'table',
			header: {
			values: [["Low"], ["Mid"], ["High"], ["Market"]],
			align: "center",
			line: {width: 1, color: 'black'},
			fill: {color: "grey"},
			font: {family: "Arial", size: 12, color: "white"}
			},
			cells: {
			values: values,
			align: "center",
			line: {color: "black", width: 1},
			font: {family: "Arial", size: 11, color: ["black"]}
			}
	}]

	Plotly.plot('table', data);

	//Check if image already exists
	if (document.getElementById('cardImgId') !== null) {
		var element = document.getElementById('cardImgId');
		element.parentNode.removeChild(element);
	}
	//Add image
	var cardimg = document.createElement("img");
	cardimg.id = 'cardImgId';
	cardimg.src = newString[0];
	var imgLoc = document.getElementById("cardImgDiv");
	imgLoc.appendChild(cardimg);
}