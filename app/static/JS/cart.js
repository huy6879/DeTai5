function addToCart(id, D_air, A_air, T_time, price){

    fetch('/api/add-cart', {
        method: 'post',
        body: JSON.stringify({
            'id': id,
            'D_air': D_air,
            'A_air': A_air,
            'T_time': T_time,
            'price': price
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(function(res) {
        console.info(res)
        return res.json()
    }).then(function(data) {
        console.info(data)
    }).catch(function(err) {
        console.error(err)
    })
}