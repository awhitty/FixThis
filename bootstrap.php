<?php
require 'Slim/Slim.php';
\Slim\Slim::registerAutoloader();

$app = new \Slim\Slim();
$app->get('/', function () {
    echo "Hello, world";
});

$app->get('/:name', function ($name) {
    echo "Hello, $name";
});
$app->run();

?>