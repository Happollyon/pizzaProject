var script = document.createElement('script');
script.src = 'https://code.jquery.com/jquery-3.4.1.min.js';
script.type = 'text/javascript';
document.getElementsByTagName('head')[0].appendChild(script);

// the code above includes the jquery cdn to the document




// this function displays the detais of clicked item in the menu
function show_details(event)
 {
 
	let item = event.currentTarget;
	item.querySelector(".size").style.display='flex';		item.querySelector(".topping").style.display='flex';
	item.querySelector(".button").style.display="flex";	  
 }

// this function gets the tokent to send back to server
function getCookie(name) {
	    var cookieValue = null;
	    if (document.cookie && document.cookie !== '') {
		            var cookies = document.cookie.split(';');
		            for (var i = 0; i < cookies.length; i++)
		    	{
				var cookie = cookies[i].trim();
	
		             if (cookie.substring(0, name.length + 1) === (name + '=')) {
		            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
		           break;
		        }
		     }
		 }
		 return cookieValue;
		 }
		

// this function limts the amount of toppings the user can select
function limit(event)
{
	let limit =3;
	

	console.log($(event.currentTarget).siblings(':checked').length)
	if($(event.currentTarget).siblings(':checked').length >= limit-1) {
		        this.checked = false;
		alert('ok')
	 }

}


// this function adds item to basket
function regular_pizza(item)
{
	var csrftoken = getCookie('csrftoken');
	let topping=''	
	let item_obj=document.getElementById(item)
	let size=''

	var xhttp = new XMLHttpRequest();
	  xhttp.onreadystatechange = function() 
	       	{
		      if (this.readyState == 4 && this.status == 200) 
		  {
			  alert('1')
	          }
		    };
	

	let data ={tp1:"chees", tp2:"bacon",tp3:"tomato"}
	data = JSON.stringify(data)
	xhttp.open("POST", "/reg_pizza", true);
	xhttp.setRequestHeader("Content-type", "application/json");  
	xhttp.setRequestHeader("X-CSRFToken",csrftoken)
	xhttp.send(data);
}
function sici_pizza()
{
	let topping=''
	let item=''
	let size=''
}
function pasta()
{
	let item=''
}

function salad()
{
		let item=''
}	

function platter()
{
	let item=''
	let size=''
}
