import jsQR from "jsqr";
import arDrone from "ar-drone";
import cv from "opencv"
import * as cloner from "cloner";

cv.readImage('plates.jpeg', function (err, mat)
{
    mat.convertGrayscale();
    mat.medianBlur(5);
    console.log(mat);
    //let circles = mat.houghCircles(1.3, mat.size()[0]/8);
    let circles = mat.houghCircles(1.2, 100);

    console.log(circles);
    for (let i=0; i<circles.length; i++){
        let x = circles[i];
        let circleCenterX = x[0];
        let circleCenterY = x[1];
        let circleRadius = x[2];
        console.log(circles);
        mat.ellipse(circleCenterX, circleCenterY, circleRadius, circleRadius);
    }
    mat.save('./circles.jpg');

    // Do something with the circles
});
/*

let drone = arDrone.createClient();

let s = new cv.ImageStream();

s.on('data', function(matrix){
    console.log(matrix);
    let circles = matrix.houghCircles(1, 1);
    // Do something with the circles

    if(circles.length >= 1) {
        console.log(circles);
    }
});


drone.getPngStream().pipe(s);
*/