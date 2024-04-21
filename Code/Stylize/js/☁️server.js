//
//	☁️server.js
//	landingpager
//
//	Created by Shaunak Ghosh on 10/11/2023.
//
//

const http = require("http");
const host = 'localhost';
const port = 8000;
const name = "INSERT_NAME_HERE";

const requestListener = function (req, res) {
	res.writeHead(200);
	res.end("landingpager server is running!");
	res.end(name)
};

const server = http.createServer(requestListener);
server.listen(port, host, () => {
	console.log(`Server is running on http://${host}:${port}`);
});