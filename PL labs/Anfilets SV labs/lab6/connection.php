<?php
	$connection = mysqli_connect('127.0.0.1', 'root', 'root', 'sessions');
	if($connection == false){
		echo mysqli_connect_error();
		die("crap");
	}
?>