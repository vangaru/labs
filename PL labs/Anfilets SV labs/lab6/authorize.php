<?php
	include('connection.php');

	session_start();

	if(isset($_POST['submit'])){
		$login = mysqli_real_escape_string($connection, $_POST['login']);
		$query_text = "SELECT * FROM `users` WHERE `login` = '$login' LIMIT 1";
		$query = mysqli_query($connection, $query_text);

		$user_data = mysqli_fetch_assoc($query);

		if($user_data['password'] == $_POST['password']){
			if($user_data['type'] == 'common'){
				$_SESSION['common_user_id'] = $user_data['id'];
				$_SESSION['common_user_login'] = $user_data['login'];
				header("Location: commonuserpage.php");
				exit();
			}
			elseif($user_data['type'] == 'admin'){
				$_SESSION['admin_user_id'] = $user_data['id'];
				$_SESSION['admin_user_login'] = $user_data['login'];
				header("Location: adminuserpage.php");
				exit();
			}
			else{
				echo "Неизвестная ошибка";
				die();
			}
		}
		else{
			echo "<h3>Внимание</h3>" . "<br/>";
			echo "Неверный пароль";
		}
	}
?>