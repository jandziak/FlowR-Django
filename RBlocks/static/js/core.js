
/**
 *
 *	connectionData(Host, Port, path)
 */

function RB_init(debug , connectionData)
{
	this.debug = debug;
	this.connectionData;
	
}


RB_init.prototype = {
};

/**
 *
 *
 */
 
 
 function RB_connect_2_srv(connectionData, debug)
 {
	this.connectionData = connectionData;
	this.webSocket;
	this.debug = debug;
 }
 
 RB_connect_2_srv.prototype = {
 
	constructor:  RB_connect_2_srv,
	connect:function ()
	{
		this.webSocket = new WebSocket("https://" + connectionData[0] + ":" +  connectionData[1] + connectionData[2]);
		
		if(this.webSocket != null)
		{
			
			this.webSocket.onopen = function()
			{
				//JSON.stringify
			}
			
			this.webSocket.onmessage = function (evt) 
			{ 
				
				if(debug == 1)
					console.log(JSON.parse(evt.data));
			};
			
			this.webSocket.onclose = function()
			{ 
				// websocket is closed.
				alert("Connection is closed..."); 
			};
			
			
			
			//TODO: ErrorCode
			return true;
		}
		else
		{
			//TODO: ErrorCode
			return false;
		}
	},
	send:function(data)
	{
			this.webSocket.send(JSON.stringify(data));
	}
 }
 
 
 
 
 /**
  *
  *
  *
  */
 function RB_block(type, options)
 {
	 this.Type = type;
	 
	 this.options = options;
	 this.id;
	 
	 this.linkIN;
	 this.linkOUT;
	 
 }
 
 
 
	$('.RB_elem__block').draggable({
		containment: "parent"
	});
	
  $(".RB_elem_popup").draggable({
	  containment: "#RB_mainBlock__content"
  });


 $('.RB_elem__block').dblclick(function(e){
	y = e.target;
	type = y.getAttribute('type');
	x = $('.' +  type + '_pop');
	if(x[0].style.display == "" || x[0].style.display == "none"){
			$('.' +  type + '_pop').css("display", "block");
	}
	else{
		$('.' +  type + '_pop').css("display", "none");
	};
});	
 $('.RB_elem_popup').dblclick(function(){
	x = $('.' +  type + '_pop');
	 if(x[0].style.display ==  "block"){
		 $('.' +  type + '_pop').css("display", "none");
	 };
});


