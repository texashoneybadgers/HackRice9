const mongoose = require('mongoose');

let Schema = mongoose.Schema;

const lockSchema = new Schema({
	name: String,
	location: String,
	status: Number,
	reserved: Number
});

const Lock = mongoose.model('Lock', lockSchema);

module.exports = Lock;
