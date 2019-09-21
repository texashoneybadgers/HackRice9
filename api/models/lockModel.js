var mongoose = require('mongoose');

// Setup schema
var lockSchema = mongoose.Schema({
	name: {
		type: String,
		required: true
	},
	location: {
		type: String,
		required: true
	},
	status: {
		type: Number,
		required: true
	},
	reserved: Number
});

// Export lock model
var Lock = module.exports = mongoose.model('lock', lockSchema);

module.exports.get = function (callback, limit) {
	Lock.find(callback).limit(limit);
};
