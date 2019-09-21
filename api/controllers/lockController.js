// Import lock model
Lock = require('../models/lockModel');

// Handle index actions
exports.index = function(req, res) {
	Lock.get(function(err, locks) {
		if (err) {
			res.json({
				status: "error",
				message: err,
			});
		}
		res.json({
			status: "success",
			message:" Locks retrieved successfully",
			data: locks
		});
	});
};

// Handle create lock actions
exports.new = function(req, res) {
	var lock = new Lock();
	lock.name = req.body.name ? req.body.name : lock.name;
	lock.location = req.body.location;
	lock.status = req.body.status;
	lock.reserved = req.body.reserved;

	// save the lock and check for errors
	lock.save(function (err) {
		if (err)
			res.json(err);
		res.json ({
			message: 'New lock created!',
			data: lock
		});
	});
};

//Handle view lock info
exports.view = function (req, res) {
	Lock.findById(req.params.lock_id, function(err, lock) {
		if (err)
			res.send(err);
		res.json({
			message: 'Lock details loading..',
			data: lock
		});
	});
};

exports.update = function(req, res) {
	Lock.findById(req.params.lock_id, function(err, lock) {
		console.log("got here");
		if (err)
			res.send(err);
		lock.name = req.body.name ? req.body.name : lock.name;
		lock.location = req.body.location;
		lock.status = req.body.status;
		lock.reserved = req.body.reserved;

		//save the lock and check for errors
		lock.save(function(err) {
			if (err)
				res.json(err)
			res.json({
				message: 'Lock Info updated',
				data: lock
			});
		});
	});
};

// Handle delete lock
exports.delete = function(req, res) {
	Lock.remove({
		_id: req.params.lock_id
	}, function (err, contact) {
		if (err)
			res.send(err);
		res.json({
			status: "success",
			message: 'Lock deleted',
		});
	});
};
