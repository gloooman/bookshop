let cartAdds = document.querySelectorAll('.form-buy');

for (const cartAdd of cartAdds) {
    cartAdd.addEventListener('submit', function (e) {
        e.preventDefault();
        let id = cartAdd.dataset.id;
        let name = cartAdd.dataset.name;
        let price = cartAdd.dataset.price;
        let author = cartAdd.dataset.author;
        let image = cartAdd.dataset.image;
        let url = cartAdd.getAttribute('action');

        fetch(url, {
            method: "POST",
            body: new FormData(cartAdd)
        })
            .then(response => response.json())
            .then(function (json) {
                let quantity = json.quantity;
                if (document.getElementById('cart-id-' + id)) {
                    let li = document.getElementById('cart-id-' + id);
                    let quantityElement = li.querySelector('.quantity');
                    let quantityNew = parseInt(quantityElement.textContent) + parseInt(quantity);
                    quantityElement.textContent = quantityNew
                } else {
                    let li_new = document.createElement('li');
                    li_new.classList.add('list-group-item', 'list-group-item-action', 'list-group-item-secondary');
                    li_new.id = 'cart-id-' + id;
                    li_new.innerHTML = `<div class="media position-relative">
                <img src="/${image}" class="align-self-center img-fluid" style="max-height: 75px;">
                <div class="media-body m-1"><p>${name} (${author})</p>
                Количество: <span class="quantity">${quantity}</span>, Цена: ${price} грн. 
                 <a href="" class="close" style="color: red">&times;</a>
                    
                </div>
            </div>`;
                    item_list.append(li_new);
                    document.getElementById('cart-length').textContent =
                        parseInt(document.getElementById('cart-length').textContent) + 1;
                    li_new.querySelector('.close').addEventListener('click', function (e) {
                        e.preventDefault();
                        let url = '/order/remove/'+id+'/';
                        console.log(url);
                        fetch(url)
                            .then(response => response.json())
                            .then(function (json) {
                                li_new.remove();
                                document.getElementById('cart-length').textContent =
                                    parseInt(document.getElementById('cart-length').textContent) - 1;
                            })
                            .catch(function (error) {
                                console.log(error)
                            });
                    })
                }
            })
            .catch(function (error) {
                console.log(error);
            });
    });
}


let cartRemoves = document.querySelectorAll('.close');

for (const cartRemove of cartRemoves){
    cartRemove.addEventListener('click', function (e) {
        e.preventDefault();

        let url = cartRemove.getAttribute('href');
        console.log(url+' is end');
        fetch(url)
            .then(response => response.json())
            .then(function (json) {
                document.getElementById('cart-id-'+json.product_id).remove()
                document.getElementById('cart-length').textContent =
                    parseInt(document.getElementById('cart-length').textContent) - 1
            })
            .catch(function (error) {
                console.log(error);
            });
    })
}


