<?php
	include('connection.php');

	if(isset($_POST['submit'])){
		$err = [];

		if(!preg_match("/^[a-zA-Z0-9]+$/", $_POST['login'])){
			$err[] = "Логин может состоять только из букв английского алфавита и цифр";
		}

		if(strlen($_POST['login']) < 3 or strlen($_POST['login']) > 30){
			$err[] = "Логин должен быть в пределах 3-30 символов";
		}

		$query = mysqli_query($connection, "SELECT `id` FROM `users` WHERE login='".mysqli_real_escape_string($connection, $_POST['login'])."'");
		if(mysqli_num_rows($query) > 0){
			$err[] = "Пользователь с таким именем уже существует";
		}

		if(count($err) == 0){
			$login = $_POST['login'];
			$password = $_POST['password'];

			$query = mysqli_query($connection, "INSERT INTO `users` VALUES(NULL, '$login', '$password', 'common')");
			header("Location: login.php");
			exit();
		}
		else{
			echo "<h3>Внимание:</h3>";
			foreach ($err as $e) {
				echo $e . "<br/>";
			} 
		}
	}
?>