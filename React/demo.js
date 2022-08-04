// let hello = function(name){
//     console.log("Hello " + name);
//     console.log(`Hello ${name}!`);
// }

// let helloAgain = (name,role) => {
//     console.log(`Hello ${name}`);
//     console.log(`You're an ${role}`);
// }

// hello('Emily');
// helloAgain('Danai','instructor')

class Fruit{
    constructor(name = 'fruit'){
        this.name = name;
    }
    nameFruit(){
        console.log(`The fruit is ${this.name}`);
    }

    whatIsThis = () => console.log(this);
}

class Apple extends Fruit{
    constructor(name){
        super(name);
        this.color = 'red';
    }

    whatColor = () => console.log(this.color)
}

let fruit = new Fruit();
fruit.nameFruit();

let apple = new Apple('Apple');
apple.nameFruit();