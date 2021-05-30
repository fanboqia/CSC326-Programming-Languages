<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Frames</title>
</head>

<style>
	
	#results{
		padding:5px;
		line-height: 15px;
		height:15px;
		border: solid 5px #008080;
		color: #fff;
		background: #a7dbd5;
		font-size: 30px;
	}

	#results td{
		border: solid 3px #008080;
		padding:5px;
		background: #a7dbd5;
		text-align: center;
		font-size: 30px;
	}

</style>
<body>

	<table id ="results">
		<th>Word</th>
		<th>Count</th>

		% for keyword in keyListInInputOrder:
		<tr>
			<td>{{keyword}}</td>
			<td>{{keyDic[keyword]}}</td>
		</tr>
		% end

	</table>

	<!-- <p>this is results page!</p> -->
</div>
</body>
</html>