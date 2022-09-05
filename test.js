

function Product(name, price) {

  this.name = name;

  this.price = price;

}


function Food(name, price) {

  Product.call(this, name, price);

  this.category = 'food';

}



var bread = new Food('pão', 'cinco reais');

console.log(bread instanceof Product);
