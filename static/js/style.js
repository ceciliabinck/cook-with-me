$(document).ready(function(){
    $('select').formSelect();
    $('.sidenav').sidenav();
     $('.tabs').tabs();
    $('.carousel').carousel();
});

/*
** Add extra field ingredients in add_recipe
*/
$(document).ready(function() {
	var max_fields      = 25; //maximum input boxes allowed
	var wrapper   		= $(".input_field_wrap"); //Fields wrapper
	var add_button      = $(".adding_field_button"); //Add button ID
	
	var x = 1; //initlal text box count
	$(add_button).click(function(e){ //on add input button click
		e.preventDefault();
		if(x < max_fields){ //max input box allowed
			x++; //text box increment
			$(wrapper).append('<div><input type="text" name="ingredients[]"/><a href="#" class="delete_field">Remove</a></div>'); //add input box
		}
	});
	
	$(wrapper).on("click",".delete_field", function(e){ //user click on remove text
		e.preventDefault(); $(this).parent('div').remove(); x--;
	})
});

/*
** Add extra field ingredients in edit_recipe
*/
$(document).ready(function() {
	var max_fields      = 25; //maximum input boxes allowed
	var wrapper   		= $(".input_field_wraps"); //Fields wrapper
	var add_button      = $(".addings_field_button"); //Add button ID
	
	var x = 1; //initlal text box count
	$(add_button).click(function(e){ //on add input button click
		e.preventDefault();
		if(x < max_fields){ //max input box allowed
			x++; //text box increment
			$(wrapper).append('<div><input type="text" name="ingredients[]"/><a href="#" class="delete_field">Remove</a></div>'); //add input box
		}
	});
	
	$(wrapper).on("click",".delete_field", function(e){ //user click on remove text
		e.preventDefault(); $(this).parent('div').remove(); x--;
	})
});

/*
** Add extra field method in add_recipe
*/
$(document).ready(function() {
	var max_fields      = 25; //maximum input boxes allowed
	var wrapper   		= $(".input_fields_wrap"); //Fields wrapper
	var add_button      = $(".add_field_button"); //Add button ID
	
	var x = 1; //initlal text box count
	$(add_button).click(function(e){ //on add input button click
		e.preventDefault();
		if(x < max_fields){ //max input box allowed
			x++; //text box increment
			$(wrapper).append('<div><input type="text" name="method[]"/><a href="#" class="remove_field">Remove</a></div>'); //add input box
		}
	});
	
	$(wrapper).on("click",".remove_field", function(e){ //user click on remove text
		e.preventDefault(); $(this).parent('div').remove(); x--;
	})
});


/*
** Add extra field method in edit_recipe
*/
$(document).ready(function() {
	var max_fields      = 25; //maximum input boxes allowed
	var wrapper   		= $(".input_fields_wraps"); //Fields wrapper
	var add_button      = $(".adds_field_button"); //Add button ID
	
	var x = 1; //initlal text box count
	$(add_button).click(function(e){ //on add input button click
		e.preventDefault();
		if(x < max_fields){ //max input box allowed
			x++; //text box increment
			$(wrapper).append('<div><input type="text" name="method[]"/><a href="#" class="remove_field">Remove</a></div>'); //add input box
		}
	});
	
	$(wrapper).on("click",".remove_field", function(e){ //user click on remove text
		e.preventDefault(); $(this).parent('div').remove(); x--;
	})
});