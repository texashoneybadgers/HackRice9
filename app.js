// Import express
let express = require('express');
// Import body-parser
let bodyParser = require('body-parser');
// Import Mongoose
let mongoose = require('mongoose');
//Initialise app
let app = express();

// Import routes
let apiRoutes = require('./api/routes/lockRoute');

// Configure body parser to handle post requests
app.use(bodyParser.urlencoded({
	extended: true
}));

app.use(bodyParser.json());

// Connect to Mongoose and set connection variable
mongoose.connect('mongodb://localhost/rice', {useNewUrlParser: true});
var db = mongoose.connection;

// Checking for database connection
if (!db)
	console.log("Error connecting to the database!")
else
	console.log("Connected to the database successfully")

// Setup server port
var port = process.env.PORT || 8080;

//Use API routes in the app
app.use('/api', apiRoutes);
//Launch app to listen to specified port
app.listen(port, function() {
	console.log('Running LockRice on port ' + port);
});
