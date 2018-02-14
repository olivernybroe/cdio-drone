import jsQR from "jsqr";
import arDrone from "ar-drone";

let client = arDrone.createClient();


let pngStream = client.getPngStream();


pngStream.on('data', function (data) {
    console.log(data.constructor.name);
    console.log(jsQR());
});



