var arDrone = require('ar-drone');
var client  = arDrone.createClient();

client.takeoff(function () {
    
});

client
    .after(5000, function() {
        this.front(0.2)
    })
    .after(4000, function() {
        this.stop();
        this.land();
    });