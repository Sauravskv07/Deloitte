const User =require("./models").User;
const States=require('./models').States;
const Markets= require('./models').Markets;
const Varieties =require('./models').Varieties;
const Grades= require('./models').Grades;
const ErrorHandler=require("../_helpers/error-handler");
const express=require('express');
const router=express.Router();
const path=require('path');
const queue=[];

router.get('/home',(req,res)=>{

    req.user = req.session.user;
    
    if(req.user)
    {
        return res.render('home', {user: req.session.user,states:States, grades:Grades, varieties:Varieties, markets:Markets})
    }
    else
    {
            return res.render('index',{user: req.session.user,states:States, grades:Grades, varieties:Varieties, markets:Markets});
    }

})

router.post('/home',(req,res)=>{

    req.user = req.session.user;
    
    if(req.user)
    {
        return res.render('home', {user: req.session.user,states:States, grades:Grades, varieties:Varieties, markets:Markets})
    }
    else
    {
            return res.render('index',{user: req.session.user,states:States, grades:Grades, varieties:Varieties, markets:Markets});
    }

})

router.get('/',(req,res)=>{

        return res.render('index',{user: req.session.user,states:States, grades:Grades, varieties:Varieties, markets:Markets});
  })


router.get('/blog',(req,res)=>{

		return res.render('blog',{user: req.session.user,states:States, grades:Grades, varieties:Varieties, markets:Markets});
})
module.exports=router;