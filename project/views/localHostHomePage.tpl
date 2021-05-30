<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Google</title>
</head>
<link rel="stylesheet" href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
<script src="https://code.jquery.com/jquery-1.12.4.js"></script>
<script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
<script>
//https://stackoverflow.com/questions/3286874/remove-all-multiple-spaces-in-javascript-and-replace-with-single-space
// var str = "  toronto is    food  isn't it?";
// str = str.replace(/ +(?= )/g,'');
// str = str.trim()
// console.log(str)

// var x = document.cookie;
// console.log('cookie:' + x);

var availableTags;

//reference on http://jqueryui.com/autocomplete/
$(function() {

	  // console.log($('.searchWordList td').html());
	  // console.log(childNodeTableSearchHistory.length);
	  // console.log('hhhh' + childNodeTableSearchHistory.innerHTML);
	 //  console.log(document.getElementById('wow'));
	 // var keywords = document.getElementById('wow').childNodes
	 // var i;
	 // var arrKeys = [];
 	//    for (i = 0; i < keywords.length; i++) {
  	//  	    arrKeys.push(keywords[i].innerHTML);
  	//    }
 	 //    console.log(arrKeys)
	 //var keyword = $('.searchWordList')children().html();

	  var childNodeTableSearchHistory = $('.searchWordList td');

  	  availableTags = [];

  	  var i;
  	  for(i = 0; i < childNodeTableSearchHistory.length; i++){
  	  		availableTags.push(childNodeTableSearchHistory[i].innerHTML);
  	  		console.log(childNodeTableSearchHistory[i].innerHTML);
  	  }

    //availableTags.push(keyword);

    $( "#frame" ).autocomplete({
      source: availableTags
    });

 //    function getWords(){
	// var inputSearchWords = $('#frame').val().trim();
	// inputSearchWords = inputSearchWords.replace(/ +(?= )/g,'');
	// inputSearchWords = inputSearchWords.split(" ")
	// availableTags.concat(inputSearchWords);
	// console.log(availableTags)
	// }
} );


// function logOutGoogle(){
// 	//document.getElementById('logout').innerHTML = "asdasdasdas"
//     // setTimeout(function(){ 
//     //  window.location.href = "http://localhost:8080";
//     //  }, 1000);
//     //use appengine as a middle website to log out all the device logged in with google and then redirect to my website
//     //reference on stackoverflow https://stackoverflow.com/questions/10650673/https-www-google-com-accounts-logout-clears-all-the-google-cookies-in-browse
//     document.location.href = "https://www.google.com/accounts/Logout?continue=https://appengine.google.com/_ah/logout?continue=http://localhost:8080/logout";
// }

function pixelDection(){
	var width = window.outerWidth;
	var height = window.outerHeight;

	var iconToMove = $("#iconToMove");
	var searchInputBox = $('#searchInputBox');
	var submitButtonDiv = $('#divOfSubmitButton');
	var submitButton = $('#submitButton');

	if(width < 768){
		iconToMove.css({height: '120px'});
		searchInputBox.css({width: '50%'});
		submitButtonDiv.css({width:'50%'});
		submitButton.css({width:'50%'});
	}else{
		submitButton.css({width:'40%'});
	}
}

$(document).ready(function(){

	var width = window.outerWidth;
	var height = window.outerHeight;

	var iconToMove = $("#iconToMove");
	var searchInputBox = $('#searchInputBox');
	var divOfSubmitButton = $('#divOfSubmitButton');

	//for animate logic
	if(width >= 768){

		iconToMove.animate({
			height: '120px'
		}, 500);

		searchInputBox.animate({
			width: '40%'
		}, 500);

		divOfSubmitButton.fadeIn(1500);
	
	}
});

</script>

<style>

body{

}
	 
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

.showhands:hover{
	cursor: pointer;
}

/*responsive web design*/
/*for pc*/
@media only screen and (min-width: 768px){
	#searchInputBox{
		width: 0;
		display: inline-block;
	}
	.divOfSubmitButton{
		width: 100%;
		display: inline-block;
	}
	#submitButton{
		display: inline-block;
		width: 20%;
	}
	#frame{
		display: inline-block;
		width: 95.5%;
	}
	.controlIcon{
		position: relative;
		left: -5%;
		width: 120%;
		height: 150%;
		z-index: -1;
	}
	#icon{
		width: 120%; 
		height: 150%;
	}
}

/*for tablet*/
@media only screen and (min-width: 600px) and (max-width: 768px){
	#searchInputBox{
		display: block;
		width: 50%;
	}
	#frame{
		width: 93.5%;
	}
	#submitButton{
		display: block;
		width: 50%;
	}
	#icon{
		width: 200%; 
		height: 200%;
		left: 20%;
	}

	.controlIcon{
		position: relative;
		left: -13%;
	}
}

/*for cellphone*/
@media only screen and (max-width: 600px){

	#searchInputBox{
		display: block;
		width: 50%;
	}
	#frame{
		width: 91%;
	}
	#submitButton{
		display: block;
		width: 52%;
	}
	#icon{
		width: 200%; 
		height: 200%;
		left: 20%;
	}
	.controlIcon{
		position: relative;
		left: 10%;
		z-index: -1;
	}

}


/*when button encounters the google translator*/
@media only screen and (max-width: 342px){

	#logout{
		padding-top: 10px;
		clear:both;
		position: relative;
		right: -10px;
	}
}


</style>
<body onresize="pixelDection()" onload="pixelDection()">

<!--google language switch plugin!-->
<div id="google_translate_element" style="float:left"></div><script type="text/javascript">
function googleTranslateElementInit() {
  new google.translate.TranslateElement({pageLanguage: 'en', layout: google.translate.TranslateElement.InlineLayout.SIMPLE}, 'google_translate_element');
}
</script><script type="text/javascript" src="//translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>
<!--cool stuff-->

<div class = "signInLogout">
	<div style="padding-left: 10px; z-index: 2" class = "showhands" id = "signin">
	<form action = "/signin" method="POST" class = "showhands">
		<input type="submit" value = "Sign in" style="float: right; width: 70px; height: 30px; background: #4987ee; color: white; font-family: arial,sans-serif; font-size: 14px; font-weight: bold; outline: none; border-style: none;" spellcheck="true">
	</form>
	</div>
	<div style="float: right; z-index: 2" class = "showhands" id = "logout">
	<form action = "/logout" id = "logout" method="GET" style="padding-right: 20px" class = "showhands">
		<input type="submit" value = "Sign out" style = "width: 70px; height: 30px; background: #4987ee; color: white; font-family: arial,sans-serif; font-size: 14px; font-weight: bold; outline: none; border-style: none;" spellcheck="true">
	</form>
<!-- 	<button onclick = "logOutGoogle()" value = "logout" style = "float: right; width: 70px; height: 30px; background: #4987ee; color: white; font-family: arial,sans-serif; font-size: 14px; font-weight: bold; outline: none; border-style: none;">Logout</button> -->
	</div>
</div>

<div class = "controlIcon">
<div style="position: relative; top: 150px; left: 20%" id = "icon">
	<img src="../static/img/googleIcon.png" alt= "icon" style = "width: 22%; height: 0" id = "iconToMove">
</div>
</div>

<div style = "position: relative; left: 25%; top: 200px" class = "showhands">
	<div>
		<form action="/search/0" method="GET" class = "showhands" style  = "border: none; ">
			<div id = "searchInputBox">
				<input id = "frame" type="text" name = "keywords" style = "height: 46px; line-height: 40px; padding-left: 20px; outline: none; font-size: 16px; color: #222; font-family: arial,sans-serif;" class = "showhands" spellcheck="true" 
					placeholder="Start Search!" onclick="this.value = ''" autocorrect = "on" autocomplete = 'on' >
			</div>
			<div class = "divOfSubmitButton" class = "showhands">
				<input id = "submitButton" type="submit" value = "Search" style = "border: 1px solid #ddd; height: 52px; font-weight: bold; font-size: 15px;color: #757575; background: #f2f2f2;" class = "showhands" 
				    spellcheck="true">
			</div>
		</form>
	</div>

<!-- 	<div style="float: left" top: 10px">
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
	</div> -->

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
	% end

	%if searchword != None:
	<div style="float: left; padding-right: 40px">	
		<table class = "searchWordList">
		<th style="padding-right: 40px">Search Words</th>
			% for keyword in searchword:
				<tr>
					<td class = 'keywordContent'>{{keyword}}</td>
				</tr>
			% end
		</table>
	</div>
	% end

</div>

<!-- <div class = "timer" style="position: absolute; top: 6%; right: 0; z-index: 2; background: #4d89eb; color: white; font-weight: bold; padding: 10px; font-family: arial,sans-serif; font-size: 14px; ">
<span>Toronto: </span>
<span id="Toronto_z18a"></span>
<script src="//widget.time.is/t.js"></script>
<script>
time_is_widget.init({Toronto_z18a:{time_format:"12hours:minutes:secondsAMPM"}});
</script>
</div>
 -->
<!--paint after the above to prevent blocking drawing-->
% if user_email != None:
<div style = "position: absolute; top: 5%; left:0;">
	% if picture != None:
	<img src="{{picture}}" alt="userPhoto" style = "width: 50px;height: 50px; border-radius: 50%; border: rgb(60, 179, 113) solid 2px">
	% end
	% if user_email != None:
	<span style = "color: #4d89eb; position: absolute; top: 17px; left: 60px; text-shadow: 1px 1px #ddd;"><b>{{user_email}}</b></span>
	% end
	% if name != None:
	<span>{{name}}</span>
	% end
</div>
% end 

</body>
</html>