import './App.css';
import AskWord from './AskWord';
//import MenuMUI from "./MUI/MenuMUI";

function App() {

function Word(word, definition) {
	this.word = word;
	this.definition = definition;
}

var abc = "abccdefghijklmnopqrstuxyz"
var wordList = []

for (var l in abc) {
	let path = './data/' + abc[l] + '.json'
	//console.log(path)
	const jsonData = require('' + path); 	
	for (var i in jsonData){
		
		if (jsonData[i]['word'].length === 5){
			const word = new Word(jsonData[i]['word'],jsonData[i]['meanings'][0]['def'])
			//console.log(jsonData[i]['word'])
			wordList.push(word)
		}
	}
		
}

//console.log(wordList[20])




  return (
    <div className="App">
    <AskWord wordList={wordList}/>
    </div>
  );
}

export default App;
