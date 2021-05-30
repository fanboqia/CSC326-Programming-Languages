<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Search</title>
</head>
<link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
<script src="https://code.jquery.com/jquery-1.12.4.js"></script>
<script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>

<script>


// function getWords(){
// 	var inputSearchWords = $('#frame').val().trim();
// 	inputSearchWords = inputSearchWords.replace(/ +(?= )/g,'');
// 	inputSearchWords = inputSearchWords.split(" ");
// 	availableTags.concat(inputSearchWords);
// 	console.log(availableTags);
// }
	
var availableTags;

//reference on http://jqueryui.com/autocomplete/

$(function() {


	var childNodeTableSearchHistory = $('.searchWordList td');

  	availableTags = [];

  	var i;
  	for(i = 0; i < childNodeTableSearchHistory.length;i++){
  	  	availableTags.push(childNodeTableSearchHistory[i].innerHTML);
  	  	console.log(childNodeTableSearchHistory[i].innerHTML);
  	}

    $( "#frame" ).autocomplete({
      source: availableTags
    });
} );
</script>



<script>

function pixelDection(){
	var width = window.outerWidth;
	var height = window.outerHeight;
	console.log("current size: width: " + width + "height: " + height);

	var body = document.getElementsByTagName('body')[0];
	// body.style.width = width+"px";
	// body.style.height = height+"px";

	//phone design
	if(width <= 600){
		var signIn = document.getElementById("signIn");

		var div1 = document.getElementById("iconDiv");
		var div2 = document.getElementById("background");
		//insert div1 before the first children of body
		body.insertBefore(div1,body.childNodes[0]);
		body.insertBefore(signIn,body.childNodes[0]);
		
		$('#iconDiv').css({
			"position" : "relative",
			"left": "40%"
		});

		console.log(body);
	}else{
		var signIn = document.getElementById("signIn");

		var div1 = document.getElementById("iconDiv");
		var div2 = document.getElementById("background");
		div2.insertBefore(div1, div2.childNodes[0]);
		div2.appendChild(signIn)

		$('#iconDiv').css({
			"position" : "relative",
			"left": "1%"
		});


		console.log("body > 600px: " + body);
	}

}

//icon to redirect to homepage
function homePage(){
	//change to aws when deploy on cloud
	//http://ec2-34-234-38-53.compute-1.amazonaws.com

	console.log(window.location.href);

	var home = window.location.href;

	var newHome = '';

	for(i = 7; i < home.length; i++){
		if(home[i] != '/'){
			newHome += home[i];
		}else{
			break;
		}
	}

	newHome = 'http://' + newHome

	console.log(newHome);

	document.location.href = newHome;
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


/*responsive web design*/
/*for pc*/
@media only screen and (min-width: 768px){
	#searchInputBox{
		width: 50%;
		display: inline-block;
	}
	.divOfSubmitButton{
		width: 50%;
		display: inline-block;
	}
	#submitButton{
		width: 20%;
	}
	#frame{
		width: 97%;
		height: 42px;
	}
	#icon{
		left:35%;
		width: 10%; 
		height: 10%;
	}
}

/*for tablet*/
@media only screen and (min-width: 600px) and (max-width: 768px){
	#searchInputBox{
		width: 50%;
	}
	#frame{
		width: 93.5%;
		height: 42px;
	}
	#submitButton{
		width: 50%;
	}
	#icon{
		width: 10%; 
		height: 10%;
		left: 30%;
	}
}

/*for cellphone*/
@media only screen and (max-width: 600px){
	#searchInputBox{
		width: 60%;
	}
	#frame{
		width: 93.5%;
		height: 42px;
	}
	#submitButton{
		width: 52%;
	}
	#icon{
		width: 30%; 
		height: 30%;
		left: 20%;
	}
	#iconDiv{
		
	}
	#background{
		position: relative;
		top: 50px;
		height: 100px;
	}
	body{
		 background : #fafafa;
		 overflow: scroll;
	}
}


</style>

<!--navi-->
<body style="margin: 0; overflow: auto;" onresize="pixelDection()" onload="pixelDection()">

<!--google language switch plugin!-->
<div id="google_translate_element" style="position: absolute;"></div><script type="text/javascript">
function googleTranslateElementInit() {
  new google.translate.TranslateElement({pageLanguage: 'en', layout: google.translate.TranslateElement.InlineLayout.SIMPLE}, 'google_translate_element');
}
</script><script type="text/javascript" src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>
<!--cool stuff-->


<div style="background: #fafafa" id = "background">
<div style="position: relative; top:20px;left:1%" class = "showHands" id = "iconDiv">
	<img src="../static/img/searchEngineAWS.png" alt= "icon" onclick = "homePage()" id = "icon">
</div>
<div style = "position: relative; left: 12%; top: -30px;">
		<form action="/search/0" method="GET">
			<div>
			<div style = "float: left" id = "searchInputBox">
				<input id = "frame" type="text" name = "keywords" style = "line-height: 25px; padding-left: 20px; outline: none; border: none; font-size: 16px; color: #222; font-family: arial,sans-serif;" spellcheck="true" placeholder="enter your text here" onclick="this.value=''" onfocus="this.value=''" value = "{{keywords}}">
			</div>
			<div class = "divOfSubmitButton">
				<input id = "submitButton" type="submit" value = "Search" style = "border: 1px solid #ddd; height: 45px; width: 100px; font-weight: bold; font-size: 15px;color: #757575; background: #f2f2f2; margin-left: -1px" spellcheck="true">
			</div>
			</div>
		</form>
</div>

% print '____', keywords

<div style="padding-left: 10px; position: absolute; top:20px; right:5%; z-index: 3" id = "signIn">
	% if picture == None:
	<form action = "/signin" method="POST" class = "showHands">
		<input type="submit" value = "Sign in" style="width: 70px; height: 30px; background: #4987ee; color: white; font-family: arial,sans-serif; font-size: 14px; font-weight: bold; outline: none; border-style: none;" spellcheck="true">
	</form>
	% end
	% if picture != None:
	<img src="{{picture}}" alt="userPhoto" style = "width: 40px;height: 40px; border-radius: 50%; border: rgb(60, 179, 113) solid 2px">
	% end
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
		<a href= {{url}} >{{docTitle[url]}}</a>
		<span href= {{url}} style="color: #006621; font-size: 14px;">{{url}}</span></br>
		<span style="color: #545454; font-size: small; font-family: arial,sans-serif;">{{database_urlToWords[url]}}</span>
		% print url
	% end
% end
</div>
<br>
<!--navigation bar-->
<div style = "position: relative; bottom: 10%; left: 30%;" id = "naviBar">
<div style="position: absolute; font-size: 20px; font-weight: bold;">
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
		<img src="../static/img/naviGle.png" style = "width: 45px; height: 45px; position: absolute; bottom: 25px; right: -21px" alt="gle">&raquo</a>
	</td>
		% end
</table>
</div>
</div>

<!--interact javascript with python data, bridging by innerHTML-->
%if searchword != None:
<div style = "display:none;">	
	<table class = "searchWordList">
	<th style="padding-right: 40px">Search Words</th>
			% for keyword in searchword:
				<tr>
					<td class = 'keywordContent'>{{keyword}}</td>
				</tr>
			% end
	</table>
</div>
%end
<!-- <footer style="width: 100%; height: 80px; bottom: -100px; background: #f2f2f2"></footer> -->
</body>
</html>