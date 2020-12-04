<?php
	include('connection.php');

	$user_name = mysqli_real_escape_string($connection, $_GET['user_name']);
	$query = "DELETE FROM `users` WHERE `login` = '$user_name' AND `type` = 'common'";
	$users_table = mysqli_query($connection, $query) or die("Ошибка " . mysqli_error($connection));

	header('Location: adminuserpage.php ');
?>