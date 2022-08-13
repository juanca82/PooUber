<?php
require_once('car.php');
require_once('account.php');
require_once('uberX.php');

$uberX = new UberX("4544316354", new Account ("Camilo Ocampo", "AMG777"), "Ferrari", "812 Super Fast" );
$uberX->printDataCar();


?>