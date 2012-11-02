<?php
  require '../lib/Slim/Slim.php';
  require 'dbconnect.php';
  require 'mailer.php';

  //////////////////////////////////////////////////////////////////////////
  //
  // App Instantiation and Routes
  //
  /////////////////////////////////////////////////////////////////////////

  $app = new Slim();

  // Auth
  $app->post('/auth', 'register');
  $app->put('/auth', 'login');

  // requests
  $app->get('/requests', 'getRequests');
  $app->get('/requests/area/:type', 'getRequestsByArea');
  $app->post('/requests', 'addRequest');

  $app->get('/areas/:id', 'getAreasByUserId');
  $app->post('/areas', 'addArea');

  $app->run();

  //////////////////////////////////////////////////////////////////////////
  //
  // Authentication
  //
  /////////////////////////////////////////////////////////////////////////

  function userLookup($name) {
    $sql = "select id, hash, salt from users where name=:username";

    try {
      $db = getConnection();
      $stmt = $db->prepare($sql);
      $stmt->bindParam("username",$name);
      $stmt->execute();
      $auth = $stmt->fetchObject();
      $db = null;
    } catch (PDOException $e) {
      // TODO log this error message
      // echo '{"error":{"text":'.$e->getMessage().'}}';
      return null;
    }

    return $auth;
  }

  function validateToken() {
    $request = Slim::getInstance()->request();
    $params = json_decode($request->getBody());

    try {
      $rslt = userLookup($params->username);
    } catch (PDOException $e) {
      header('HTTP/1.0 420 Enhance Your Calm', true, 420);
      echo '{"error":{"text":'.$e->getMessage().'}}';
      return false;
    }

    if (!$rslt) return null;

    $rslt_token = hash('sha256', $rslt->id.$rslt->salt.date("z"));
    if (strcmp($params->token, $rslt_token)) {
      return null;
    } else {
      return $rslt->id;
    }
  }

  function echoToken($id, $salt) {
    $token = hash('sha256', $id.$salt.date("z"));
    echo '{"token":"'.$token.'"}';
  }

  function echoError($errstr) {
    header('HTTP/1.0 420 Enhance Your Calm', true, 420);
    echo '{"error":"'.$errstr.'","token":""}';
  }

  function login(){
    $request = Slim::getInstance()->request();
    $params = json_decode($request->getBody());

    $rslt = userLookup($params->username);
    if (!$rslt) {
      echoError('Username does not exist.');
      return;
    }

    $user_hash = hash('sha256', $params->password.$rslt->salt);
    if (strcmp($user_hash, $rslt->hash)) {
      echoError('Your password is incorrect.');
    } else {
      echoToken($rslt->id, $rslt->salt);
    }
  }

  function register() {
    $request = Slim::getInstance()->request();
    $params = json_decode($request->getBody());

    $existing = userLookup($params->username);
    if ($existing) {
      echoError('Username already in use.');
      return;
    }

    // strcmp returns 0 if there is a match
    // nonzero will trigger the error
    if (strcmp($params->code, 'FixThis12')) {
      echoError('Wrong access code.');
      return;
    }

    // TODO
    // - check that email is not already in use
    // - check that email is valid
    // - send confirmation email and have a way to receive response

    $salt = hash('sha256', uniqid(mt_rand(),true));
    $hash = hash('sha256', $params->password.$salt);
    $sql = "insert into users (name, email, hash, salt)".
           "values (:name, :email, :hash, :salt)";

    try {
      $db = getConnection();
      $stmt = $db->prepare($sql);
      $stmt->bindParam("name", $params->username);
      $stmt->bindParam("email", $params->email);
      $stmt->bindParam("hash", $hash);
      $stmt->bindParam("salt", $salt);
      $stmt->execute();
      $id = $db->lastInsertId();
      $db = null;
      echoToken($id, $salt);
    } catch (PDOException $e) {
      header('HTTP/1.0 420 Enhance Your Calm', true, 420);
      echo '{"error":{"text":'.$e->getMessage().'}}';
    }
  }

  //////////////////////////////////////////////////////////////////////////
  //
  // Requests
  //
  /////////////////////////////////////////////////////////////////////////

  function getRequests(){
     $sql = "select * from requests order by timestamp";
     try{
        $db = getConnection();
        $stmt = $db->query($sql);
        $requests = $stmt->fetchAll(PDO::FETCH_OBJ);
        $db = null;
        echo json_encode($requests);
     }catch(PDOException $e){
        header('HTTP/1.0 420 Enhance Your Calm', true, 420);
        echo '{"error":{"text":'.$e->getMessage().'}}';
     }
  }

  function getRequestByUser($user){
    $sql = "select * from requests where user_id = :user";
    try {
      $db = getConnection();
      $stmt = $db->prepare($sql);
      $stmt->bindParam('user_id', $user);
      $stmt->execute();
      $requests = $stmt->fetchAll(PDO::FETCH_OBJ);
      $db = null;
      echo json_encode($requests);
    } catch (PDOException $e) {
      header('HTTP/1.0 420 Enhance Your Calm', true, 420);
      echo '{"error":{"text":'.$e->getMessage().'}}';
    }
  }

  function addRequestQuery($params) {
    $sql = "insert into requests (desc, image) values(:desc, :image)";
    try{
      $db = getConnection();
      $stmt = $db->prepare($sql);
      $stmt->bindParam("desc", $params->desc);
      $stmt->bindParam("image", $params->image);
      $stmt->execute();
      $id = $db->lastInsertId();
      $db = null;
      return $id;
    }catch(PDOException $e){
      header('HTTP/1.0 420 Enhance Your Calm', true, 420);
      echo '{"error":{"text":'.$e->getMessage().'}}';
      return null;
    }
  }

  function addRequest(){
    $id = validateToken();
    if (!$id) {
      header('HTTP/1.0 420 Enhance Your Calm', true, 420);
      echo '{"error": "invalid token"}';
      return;
    }

    $request = Slim::getInstance()->request();
    $params = json_decode($request->getBody());

    $params->id = addRequestQuery($params);

    if ($params->id) {
      echo json_encode($params);
    }
  }
