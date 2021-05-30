<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Search</title>
</head>
<script>

function homePage(){
	//change to aws when deploy on cloud
	//http://ec2-34-234-38-53.compute-1.amazonaws.com
	document.location.href = "http://localhost:8080"
}

</script>

<style>
	 
#searchInputBox{
	box-shadow: 1px 1px 4px #888888;
}

#searchInputBox:hover{
/*	outline-style: solid*/
	box-shadow: 2px 2px 8px #888888;
}

#submitButton:hover{
	background: #f6f6f6
	border: solid 2px #000;
	cursor: pointer;
}

.navigationBar{

}

.navigationTd:hover{
	text-decoration: underline;
}

.navigationTd{
	text-decoration: none;
}

.searchURL{
	position: relative;
	left:12%;
	font-size: 20px;
	font-family: arial,sans-serif;
	line-height: 1.2;
    text-align: left;
}

.searchURL a{
	text-decoration: none;
	display: block;
	margin-top: 40px;
	color: #1a0dab;
}

.searchURL a:hover{
	text-decoration: underline;
}

.searchURL a:visited{
	color:rgb(102, 0, 153);
}

.showHands:hover{
	cursor: pointer;
}

</style>

<!--navi-->
<body style="margin: 0">
<div style="background: #fafafa">
<div style="position: relative; top:20px;left:1%" class = "showHands">
	<img src="../static/img/searchEngineAWS.png" alt= "icon" style = "width: 120px; height: 44px" onclick = "homePage()">
</div>

<div style = "position: relative; left: 12%; top: -30px;">
	<div>
		<form action="/search/0" method="GET">
			<div style = "float: left;" id = "searchInputBox">
				<input id = "frame" type="text" name = "keywords" style = "width: 585px; height: 42px; line-height: 25px; padding-left: 20px; outline: none; border: none">
			</div>
			<div class = "divOfSubmitButton">
				<input id = "submitButton" type="submit" value = "Search" style = "border: 1px solid #ddd; height: 45px; width: 100px; font-weight: bold; font-size: 15px;color: #757575; background: #f2f2f2; margin-left: -1px">
			</div>
		</form>
	</div>
</div>

<div style="padding-left: 10px; position: absolute; top:20px; right:5%">
	<form action = "/signin" method="POST" class = "showHands">
		<input type="submit" value = "Sign in" style="width: 70px; height: 30px; background: #4987ee; color: white; font-family: arial,sans-serif; font-size: 14px; font-weight: bold; outline: none; border-style: none;">
	</form>
</div>

</div>

<!--Search Key Word Not found-->
% if sortedUserURL == []:
	<div style="position: relative; left: 15%; top: 60px; font-size: 20px">
	<p>Your search - <b>{{keywords}}</b> -  did not match any documents.</p>
	<p>Suggestions: </p>
	<li>Make sure that all words are spelled correctly.</li>
	<li>Try different keywords.</li>
	<li>Try more general keywords.</li>
	<li>Try fewer keywords.</li>
	</div>
% end

<!--content-->
<div class = "searchURL">
% if sortedUserURL != []:
	% for url in sortedUserURL:
		<a href= {{url}} >{{url}}</a><br>
		% print url
	% end
% end
</div>
<!--navigation bar-->
<div style="position: absolute; bottom: 10%; left: 30%; font-size: 20px; font-weight: bold;">
<table class = "navigationBar">

	<td>
		% if pageid > 0:
		<a class = "navigationTd" href="/search/{{pageid-1}}" style="position: relative; top: 12px; right: 10px">
		<img src="../static/img/naviG.png" alt="G" style = "position: absolute; bottom: 25px; right: -8px; width: 30px; height: 30px">&laquo</a>
	</td>
		% end

	<td>
		% if pageid == 0 and sortedUserURL != []:
		<img src="../static/img/naviG.png" alt="G" style = "position: relative; bottom: 14px; left: -5px; width: 30px; height: 30px">
		% end
	</td>

% for i in range(0,pageNum):
	<td>
		<a class = "navigationTd" href= "/search/{{i}}">
			% if pageid != i: 
			<img src="../static/img/naviO.png" alt="naviO" style="width: 22px; height: 25px; position: relative; left: -5px"></br>
			% end
			% if pageid == i:
			<img src="../static/img/naviHover.png" alt="naviO" style="width: 22px; height: 29px; position: relative; left: -5px"></br>
			% end
			{{i+1}}
		</a>
	</td>
% end


	% print "pageid for next: ", pageid
	<td>
		% if pageid < pageNum - 1: 
		<a class = "navigationTd" href="/search/{{pageid+1}}" style="position: relative; top: 12px"> 
		<img src="../static/img/naviGle.png" style = "width: 45px; height: 45px; position: absolute; bottom: 15px; right: -28px" alt="gle">&raquo</a>
	</td>
		% end

	<td>
		% if pageid == pageNum - 1:
		<img src="../static/img/naviGle.png" style = "width: 45px; height: 45px; position: absolute; bottom: 21px; right: -21px" alt="gle">&raquo</a>
	</td>
		% end
</table>
</div>
</body>
</html>