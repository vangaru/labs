<?php session_start(); ?>
<!DOCTYPE html>
<html>
<head>
	<title>Привет</title>
</head>
<body>
	<?php
		include('connection.php');
		echo "<h2>Вы вошли как администратор</h2>";
		echo "Привет, " . $_SESSION['admin_user_login'];
		echo "<h1>Статистика</h1><br/>";
		$arr = file("stat.txt");
		for($i = 0; $i < count($arr); $i++){
			echo $arr[$i] . "<br/>";
		}

		$query = "SELECT * FROM `users`";
		$users_table = mysqli_query($connection, $query) or die("Ошибка " . mysqli_error($connection));

		if($users_table){

			$USERS_NICK = 1;
			$USERS_TYPE = 3;

			?>	
				<h1> Список пользователей </h1>
				<big><table>
					<tr>
						<td><b>Пользователь</b></td>
						<td><b>Тип пользователя</b></td>
					</tr>
			<?php
			$users_table_num_rows = mysqli_num_rows($users_table);
			for($i = 0; $i < $users_table_num_rows; $i++){
				$users_table_row = mysqli_fetch_row($users_table);
				?>
					<tr>
						<td><?php echo $users_table_row[$USERS_NICK]; ?></td>
						<td><?php echo $users_table_row[$USERS_TYPE]; ?></td>
					</tr>
				<?php
			}
			?> </table></big> <?php 
		}

		?> 
			<h2> Удаление пользователя </h2>
			<form method="GET" action="deleteuser.php">
				<input type="text" name="user_name" required="", placeholder="Введите имя пользователя"/>
			</form>
		 <?php

	?>
</body>
</html>