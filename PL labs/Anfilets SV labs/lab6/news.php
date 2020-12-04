<?php session_start(); ?>
<!DOCTYPE html>
<html>
<head>
	<title>Привет</title>
</head>
<body>
	<?php
		if(isset($_SESSION['common_user_login'])){
			echo "Привет, " . $_SESSION['common_user_login'];
			$file = fopen("stat.txt", "a+") or die("Не удалось открыть файл");
			$date = date('m/d/Y h:i:s a', time());
			$user_stat = $date . ": " . $_SESSION['common_user_login'] . " - news.php\n";
			fwrite($file, $user_stat);
		}
	?>
	<h1>Новости</h1>
</body>
</html>