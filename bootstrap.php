<?php
require 'lib/Slim/Slim.php';
\Slim\Slim::registerAutoloader();

$app = new \Slim\Slim();
$app->get('/', function () use ($app) {
    echo $app->render('index.html');
});

$app->post('/login/?', function () use ($app) {
    echo $app->render('index.html');
});

$app->post('/preview/', function () {
	if (!isset($_FILES['image'])) {
        echo "No image";
        return;
    }

    // TODO: Figure out file naming conventions
    if (file_exists("media/temp/" . $_FILES["image"]["name"])) {
    	echo "media/temp/" . $_FILES["image"]["name"];
    } else {
      move_uploaded_file($_FILES["image"]["tmp_name"],
      "media/temp/" . $_FILES["image"]["name"]);
      // echo "Stored in: " . "upload/" . $_FILES["file"]["name"];
    }

    echo "media/temp/" . $_FILES["image"]["name"];
});

$app->get('/api/?', function ($name) {
    echo "This is where we'll flesh out the API";
});
$app->run();