<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Google</title>
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

<div>
	<div style="padding-left: 10px; float: right;">
	<form action = "/signin" method="POST">
		<input type="submit" value = "Sign in" style="width: 70px; height: 30px; background: #4987ee; color: white; font-family: arial,sans-serif; font-size: 14px; font-weight: bold; outline: none; border-style: none;">
	</form>
	</div>
	<div style="float: right;">
	<form action = "/logout" method="GET" style="padding-right: 20px">
		<input type="submit" value = "Sign out" style = "float: right; width: 70px; height: 30px; background: #4987ee; color: white; font-family: arial,sans-serif; font-size: 14px; font-weight: bold; outline: none; border-style: none;">
	</form>
	</div>
</div>

<div style="position: relative; top:175px;left:40%">
	<img src="../static/img/googleIcon.png" alt= "icon" style = "width: 278px; height: 120px">
</div>

<div style = "position: relative; left: 25%; top: 200px">
	<div>
		<form action="" method="GET">
			<div style = "float: left;" id = "searchInputBox">
				<input id = "frame" type="text" name = "keywords" style = "width: 585px; height: 46px; line-height: 25px; padding-left: 20px; outline: none;">
			</div>
			<div class = "divOfSubmitButton">
				<input id = "submitButton" type="submit" value = "Search" style = "border: 1px solid #ddd; height: 52px; width: 100px; font-weight: bold; font-size: 15px;color: #757575; background: #f2f2f2">
			</div>
		</form>
	</div>

	<div style="float: left" top: 10px">
		<table id ="results">
		<th>Word</th>
		<th>Count</th>
	%if keyListInInputOrder != None:
		% for keyword in keyListInInputOrder:
		<tr>
			<td>{{keyword}}</td>
			<td>{{keyDic[keyword]}}</td>
		</tr>
		% end

	</table>
	</div>

	% if user_email != None:
	<div style="float: left; padding-right: 40px">	
		<table class = "history">
		<th style="padding-right: 40px">Top 20 Keywords</th>
		<th>Times</th>
 		
 		%if keyTimesTuple != None:
			% for keyword in keyTimesTuple:
			<tr>
				<td>{{keyword[0]}}</td>
				<td>{{keyword[1]}}</td>
			</tr>
			% end

		</table>
	</div>

	%if searchword != None:
	<div style="float: left; padding-right: 40px">	
		<table class = "searchWordList">
		<th style="padding-right: 40px">Search Words</th>
			% for keyword in searchword:
				<tr>
					<td>{{keyword}}</td>
				</tr>
			% end
		</table>
	</div>

</div>

<!--paint after the above to prevent blocking drawing-->
<div style = "position: absolute; top: 0; left:0">
	% if picture != None:
	<img src="{{picture}}" alt="userPhoto" style = "width: 50px;height: 50px; border-radius: 50%">
	% if user_email != None:
	<span style = "color: black; position: absolute; top: 17px; left: 60px;">{{user_email}}</span>
	% if name != None:
	<span>{{name}}</span>
</div>

</body>
</html>