module.exports = find_optimum;

var zmq = require('zeromq')

function find_optimum(product){

	var socket = zmq.socket('req');
	socket.connect("tcp://127.0.0.1:5555");
	
	socket.send(JSON.stringify(product));

	return new Promise((resolve,reject) => {
		socket.on('message',(data)=>{
			console.log(JSON.parse(data.toString()))
			resolve(data.toString());
		})
	})
}
