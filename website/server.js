const express=require('express');//, es6Renderer = require('express-es6-template-engine');   //express is used to create a server

const bodyParser=require('body-parser'); //to parser the contents of the request body

const mongoose=require('mongoose'); //an object oriented document handler

mongoose.set('bufferCommands', false);

var multer = require('multer'); //for multi content request body

const fs=require('fs'); //for internal file handling

const logger=require('morgan'); //for attractive display of logs

const {body, validationResult}=require('express-validator/check');  //for validating the contents enters

const {sanitizeBody}=require('express-validator/filter');   //for filtering malicious contents in request body

var session=require('express-session'); //for user login sessions

const config = require('./config.json');

const secret = config.secret;

const passport=require('passport');

mongoose.set('useFindAndModify', false);

mongoose.connect('mongodb+srv://dataDope:happy_cat@cluster0-u1vuz.mongodb.net/test?retryWrites=true&w=majority', {useNewUrlParser: true});

mongoose.connection.on('error',(error)=>{
    console.log("error =",error);
});

mongoose.connection.on('connected', () => {
  console.log('connected to mongodb');
});

const addTemplate=require('./routes/loginmiddlewares').addTemplate;

const app=express();    //creating the server

app.use(express.static(__dirname + '/public'));

app.use(bodyParser.json());

app.use(bodyParser.urlencoded({ extended: true }))

app.use(session(
    {   secret:secret,
        resave:true,
        saveUninitialized:true,
        name:'login',
        cookie:{expire:100000}
    })
);

// Load view engine

const path=require('path');
//app.engine('html', es6Renderer);

app.set('views', __dirname +'/views/');

require('dotenv').config();

//app.set('view engine', 'html');

app.set('view engine', 'ejs');

app.use(passport.initialize());

app.use(passport.session());

app.use(logger('dev'));

app.locals.baseURL = "http://localhost:3000/"


app.use(require('./routes/loginmiddlewares').addTemplate);
app.use(require('./routes/general'));
app.use(require('./routes/signUP'));
app.use(require('./routes/login'));
app.use(require('./routes/loginG').router);
app.use(require('./routes/loginL'));
app.use(require('./routes/forgetPassword'));
app.use(require('./routes/market'));
app.use(require('./routes/userinfo'));
app.use(require('./routes/logout'));

port = process.env.PORT || 3000
app.listen(port);

console.log('Server is listening');
