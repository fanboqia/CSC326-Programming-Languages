function logOutGoogle(){
	//document.getElementById('logout').innerHTML = "asdasdasdas"
    // setTimeout(function(){ 
    // 	window.location.href = "http://localhost:8080";
    // }, 1200);
    //use appengine as a middle website to log out all the device logged in with google and then redirect to my website
    //reference on stackoverflow https://stackoverflow.com/questions/10650673/https-www-google-com-accounts-logout-clears-all-the-google-cookies-in-browse
    document.location.href = "https://www.google.com/accounts/Logout?continue=https://appengine.google.com/_ah/logout?continue=http://localhost:8080/logout";
}
