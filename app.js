const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const Lock = require('./api/models/lock');

app.use(bodyParser.urlencoded({ extended: true}));
app.use(bodyParser.json());

mongoose.Promise = require('bluebird');
mongoose.connect('mongodb://localhost/locks');

app.use(function(req, res, next){
	console.log('we use the router, and next moves to the enxt requrests');
	next();
})

app.get('/', function(req, res) {
	res.json({ message: 'You did it! Great job!'});
});

app.get('/api/locks', function(req, res) {
	console.log('GET locks');
	Lock.find({}).then(eachOne => {
		res.json(eachOne);
	})
})

app.listen(3000);
console.log('starting application. Good job!');
