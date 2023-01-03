$(document).ready(function(){
    $('.plus-cart').click(function(){
		var id= $(this).attr("pid").toString();
		var eml= this.parentNode.children[2]
		$.ajax({
			type:'GET',
			url:'cart-plus',
			data:{
				prod_id:id
			},
			success: function(data){
				eml.innerText = data.quantity
				document.getElementById('amount').innerText=data.amount
				document.getElementById('totalamount').innerText=data.totalamount
			}
	
		})
	})
  });

  
$(document).ready(function(){
	$('.minus-cart').click(function(){
		var id= $(this).attr("pid").toString();
		var eml=this.parentNode.children[2]
		$.ajax({
			type:'GET',
			url:'cart-minus',
			data:{
				prod_id:id
			},
			success: function(data){
				eml.innerText = data.quantity
				document.getElementById('amount').innerText=data.amount
				document.getElementById('totalamount').innerText=data.totalamount
			}
		})
	})
});

$(document).ready(function(){
	$('.remove-cart').click(function(){
		var id= $(this).attr("pid").toString();
		var eml=this
		$.ajax({
			type:'GET',
			url:'cart-delete',
			data:{
				prod_id:id
			},
			success: function(data){
				
				document.getElementById('amount').innerText=data.amount
				document.getElementById('totalamount').innerText=data.totalamount
				eml.parentNode.parentNode.parentNode.parentNode.remove()
			}
		})
	})
});



  $(document).ready(function(){
    $('#myModal').on('shown.bs.modal', function () {
		$('#myInput').trigger('focus')
	  })
  });


 