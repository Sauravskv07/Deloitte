const User= require('./models').User
const States=require('./models').States;
const Markets= require('./models').Markets;
const Varieties =require('./models').Varieties;
const Grades= require('./models').Grades;
const express=require('express')
const router=express.Router()
const path=require('path')
const Optimum=require('../_helpers/find_optimum')
const ErrorHandler=require('../_helpers/error-handler')

router.get('/market',(req,res)=>{
	if(req.session.user)
		return res.render('market', {user: req.session.user,states:States, grades:Grades, varieties:Varieties, markets:Markets})
	else
		return res.render('index', {user: req.session.user,states:States, grades:Grades, varieties:Varieties, markets:Markets})
})

router.post('/market',(req,res)=>{

		console.log('request to optimum_market is')
		
		console.log(req.body)

		var optimum_markets=[];

		var products=[]

		var array_promises=[];

		var i=1;


		req.user.products.forEach((product)=>{
				//console.log(req.body["select"+i])
			if(req.body["select"+i]=='on')
			{
					
					array_promises.push(Optimum(product));

					console.log("promises array = ",array_promises);

					products.push(product);
			}

			i++;
		})

		Promise.all(array_promises).then((data)=>{

			console.log(data);

			data.forEach(optimum_market=>{
				optimum_markets.push(optimum_market.split('\n'));
				})

				console.log('optimum_markets = ',optimum_markets);
							
				return res.render('results',{user:req.session.user, products:products, optimum_markets:optimum_markets, states:States, grades:Grades, varieties:Varieties, markets:Markets})
		
			}).catch((error)=>{
					console.log('ERROR',error)
					return ErrorHandler(error,req,res);
				});

})

router.post('/post-product',(req,res)=>{

	console.log('product =',req.body);

	var product={
		market:req.body.market,
		state:req.body.state,
		grade:req.body.grade,
		variety:req.body.variety,
	}

	User.findOneAndUpdate({_id:req.user._id}, { $push: { products: product } },{new: true, upsert: true},(error,results)=>{
		if(results)
		{
			console.log('product added',results)
        	req.session.user = results;
        	res.locals.user = results;
			return res.status(200).json(results)
			//return res.render('home', {user: req.session.user,states:States, grades:Grades, varieties:Varieties, markets:Markets})
		}	
			
		else
		{
			console.log(error)
			return ErrorHandler(error,req,res)
		}
	});
})

module.exports=router