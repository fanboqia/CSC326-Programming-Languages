<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Frames</title>
</head>
<script>
</script>

<style>
	 
#searchInputBox{
	box-shadow: 2px 3px 8px #888888;
}

#searchInputBox:hover{
/*	outline-style: solid*/
	box-shadow: 5px 5px 10px #888888;
}

#submitButton:hover{
	background: #f6f6f6
	border: solid 2px #000;
}
</style>
<body>
<div style="position: relative; top:175px;left:40%">
	<img src="../static/img/googleIcon.png" alt= "icon" style = "width: 278px; height: 120px">
</div>

<div style = "position: relative; left: 25%; top: 200px">
	<div>
		<form action="/results" method="GET">
			<div style = "float: left;" id = "searchInputBox">
				<input id = "frame" type="text" name = "keywords" style = "width: 585px; height: 46px; line-height: 25px; padding-left: 20px; outline: none;">
			</div>
			<div class = "divOfSubmitButton">
				<input id = "submitButton" type="submit" value = "Search" style = "border: 1px solid #ddd; height: 52px; width: 100px; font-weight: bold; font-size: 15px;color: #757575; background: #f2f2f2">
			</div>
		</form>
	</div>
	<div style="position: relative; top: 10px">	
		<table class = "history">
		<th style="padding-right: 40px">Top 20 Keywords</th>
		<th>Times</th>
 		
		% for keyword in keyTimesTuple:
		<tr>
			<td>{{keyword[0]}}</td>
			<td>{{keyword[1]}}</td>
		</tr>
		% end

		</table>
	</div>
</div>
</body>
</html>