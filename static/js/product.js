const alertbox = document.getElementById('alert-box')



$("#mycart").click(function () {
  alert('Added to cart')
});

$('#card_it').on("click",function(e){
	$('#cartModal').show();
	e.preventDefault();
	e.stopPropagation();
});

function orderView(){
	$('#orderModal').show();
}

function OrderItem(id, quantity){

    const get_id = id
    const my_quantity = quantity
    const input_value = document.getElementById('quantity').value;

    $.ajax({
        headers: {
            "X-CSRFToken": csrftoken
        },
        type: "POST",
        url: 'cart',
        data :{
            item : id,
            input_value : input_value
        },
        success: function(data) {
            console.log(data)
			console.log("sucessfully added into cart")
			$.ajax({
				url: 'menu',
				method: 'GET',
				success: function(){
					console.log("Refreshed the cart")
                    handleAlerts("success", "Item has been added")
				},
				error: function(){
					console.log("couldn't refreshed the cart")
                    handleAlerts("error","Refresh your page")
				}

			})
        },
        error: function(result) {
            alert("error", "An error occured while adding Item in the cart");
        }
    });
}

function deleteitem(id){
	const get_id = id
    $.ajax({
        headers: {
            "X-CSRFToken": csrftoken
        },
        type: 'DELETE',
        url: 'cart/'+ id,
        data :{
            id : get_id
        },
		success: function(data){
			console.log("Item from the cart has been deleted")
		},
		error: function(data){
			console.log("Can not delete the Item")
			alert("Please try deleting the item again")
		}
});
}

const handleAlerts = (type, msg) => {
    alertbox.innerHTML = [
        `<div class="alert alert-${type} alert-dismissible" role="alert">`,
        `   <div>${msg}</div>`,
        '   <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close" onclick="buttonclose()"></button>',
        '</div>'
    ].join('')

}


function buttonclose(){ 
   alertbox.style.display = "none"; 
};  


function OrderView(){
    $.ajax({
        url: 'orders',
        method: 'GET',
        success: function(){
            console.log("Order Viewed")
        },
        error: function(){
            console.log("Something wrong occured")
            alert('something went wrong')
        }
    })
}

function logout(){
    $.ajax({
        url: 'logout',
        method: 'GET',
        success: function(){
            window.location.href="menu"
            console.log("logged out")
            handleAlerts("success", "Log out successfully")
        },
        error: function(){
            console.log("Error occured")
        }
    })




}

function OrderCreated(){
    $.ajax({
        url: 'order',
        method: 'POST',
        data: {

        },
        success: function(){
            console.log("Order created")

        },
        error: function(){
            console.log("somethng went wrong")
        }


    })
}