<?php
	class Games{
		private $games = array(0 => array('name' => 'Heavy Rain', 'developer' => 'Quantic Dreams' ),
		 					   1 => array('name' => 'Sid Meiers Civilization 5', 'developer' => 'Firaxis'));
 
		function __construct($games = array()){
			$this->games = $games;
		}

		function __destruct(){

		}

		public function set_games($games){
			$this->games = $games;
		}

		public function get_games(){
			return $this->games;
		}

		public function search_game($name){
			$names = array_column($this->games, 'name');
			$search_game_index = array_search($name, $names);
			if ($search_game_index == False){
				echo "Игра с таким названием не найдена";
				return  False;
			}
			return $this->games[$search_game_index];
		}

		public function delete_game($name){
			foreach ($this->games as $key => $game) {
				if($game['name'] == $name){
					unset($this->games[$key]);
				}
			}
		}

		public function add_game($name, $developer){
			$game = array('name' => $name, 'developer' => $developer);
			array_push($this->games, $game);
		}

		public function sortData(){
			for ($i = 0; $i < count($this->games); $i++){
				for($j = $i + 1; $j < count($this->games); $j++){
					if(strcasecmp($this->games[$i]['name'], $this->games[$j]['name']) > 0){
						$temp = $this->games[$j];
						$this->games[$j] = $this->games[$i];
						$this->games[$i] = $temp;
					}
				}
			}
		}

		public function outData(){

			?> 
			<table> 
				<tr>
					<td><b> Название </b></td>
					<td><b> Разработчик </b></td>
				</tr>
			<?php

			foreach($this->games as $game){
				?>
					<tr>
						<td><?php echo $game['name']; ?></td>
						<td><?php echo $game['developer']; ?></td>
					</tr>
				<?php
			}

			?> </table> <?php
		}

		public function saveDataToFile(){
			$file = fopen("data.txt", "w") or die("Не удалось открыть файл");
			foreach ($this->games as $game) {
				$name = $game['name'];
				$developer = $game['developer'];
				$data = "$name:$developer";
				fwrite($file, $data);
			}
		}

		public function loadDataFromFile(){
			$file = fopen("data.txt", "r");
			$this->games = array();
			while(($data = fgets($file)) !== False){
				$game_data = explode(":", $data);
				$game = array('name'=>$game_data[0], 'developer'=>$game_data[1]);
				array_push($this->games, $game);
			}
		}

		public function appendDataToFile($name, $developer){
			$file = fopen("data.txt", "a");
			$data = "$name:$developer\n";
			fwrite($file, $data);
		}

	}

	$games_obj = new Games;
	$games_obj->loadDataFromFile();
	$games_obj->outData();
	$games_obj->sortData();
	$games_obj->outData();
	$games_obj->saveDataToFile();
?>