var updateBtn = document.getElementsByClassName('update-cart'); 

for(var i = 0; i < updateBtn.length; i++) {
    updateBtn[i].addEventListener('click', function() {
        var productId = this.dataset.product;
        var action = this.dataset.action;
        console.log('Product Id : ', productId, 'Action : ', action);
        console.log('USER : ', user);
        if(user == 'AnonymousUser') {
            addCookieItem(productId, action);
        } else {
            updateUserOrder(productId, action);
        }
    })
}

function updateUserOrder(productId, action) {
    console.log('User logged in. Sending data.');

    var url = '/update_item/';
    fetch(url, {
        method : 'POST',
        headers : {
            'Content-Type' : 'application/json',
            'X-CSRFToken' : csrftoken
        },
        body : JSON.stringify({'productId': productId, 'action': action})
    })
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        console.log('data : ', data);
        location.reload();
    });
}

function addCookieItem(productId, action) {
    if(action == 'add') {
        if(cart[productId] == undefined) {
            cart[productId] =  {'quantity' : 1};
        } else {
            cart[productId]['quantity'] += 1;
        }
    }
    if(action == 'remove') {
        cart[productId]['quantity'] -= 1;
        if(cart[productId]['quantity'] <= 0) {
            console.log('Item removed.');
            delete cart[productId];
        }
    }
    console.log('Cart: ', cart);
    document.cookie = 'cart=' + JSON.stringify(cart) + ';domain=;path=/;SameSite=None;Secure';
    location.reload();
    
}