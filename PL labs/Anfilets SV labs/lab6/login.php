<!DOCTYPE html>
<html>
<head>
	<title>Войти</title>
</head>
<body>
	<h1>Войти</h1>
	<form action = "authorize.php" method = "POST">
		<input type = "text" name = "login" placeholder = "Логин"/><br/><br/>
		<input type = "password" name = "password" placeholder = "Пароль"/><br/><br/>
		<input type = "submit" value = "Отправить" name = "submit"/>
	</form>
</body>
</html>