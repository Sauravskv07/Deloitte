module.exports = find_optimum;

const spawn = require("child_process").spawn;

function find_optimum(product){

	const pythonProcess = spawn('python',["/home/sauravskv/Desktop/Deloitte/MLSTM-FCN/find_best.py", product.state, product.market, product.variety, product.grade]);

	var result = ''


	return new Promise((resolve,reject) => {
		pythonProcess.stdout.on('data', (data) => {
    		// Do something with the data returned from python script
    		result=result+data.toString()
		});	


		pythonProcess.on('close',()=>{
			console.log('resolved',result)
			resolve(result);
		})
	
		// pythonProcess.stderr.on('data',(error) => {
		// 	//reject the promise
		// 	reject(error.toString());
		// })
	})
}

