//
//	misc.js
//	landingpager
//
//	Created by Shaunak Ghosh on 10/11/2023.
//

// IMPORTS
import express from "express";

// MISCELLANEOUS FUNCTIONS
// print a debug log
function print_debug(debug) {
	const fs = require('fs') 
	console.error("STAGED ERROR: " + debug)
	fs.writeFile('debug.txt', debug, (err) => {
		// In case of a error throw err. 
		if (err) throw err; 
	}) 
}

// create a static server with a name and port.
function create_server(name, port, address) {
	const app = express();
	
	app.get('/', (req, res) => {
	  res.send('Welcome to the server!');
	  res.send(name)
	});
	
	app.listen(port, () => {
	  console.log(`Server is running on port ${port} name ${name} address ${address}`);
	});
}