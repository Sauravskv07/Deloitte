const States=require('./models').States;
const Markets= require('./models').Markets;
const Varieties =require('./models').Varieties;
const Grades= require('./models').Grades;

const express=require('express');
const router=express.Router();
const path=require('path');

router.get('/auth/login',(req,res)=>
{
    res.render('login', {user: req.session.user,states:States, grades:Grades, varieties:Varieties, markets:Markets});
})

module.exports=router;
