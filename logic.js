//let's make some lavendar ice cream
//measurements in cups, tbsp, tsp and oz
const recipe = {
    ingredients:
    {
        heavyCream: 3,
        lavender: 3,
        sweetenedCondensedMilk: 14,
        salt: 1/8,
        vanillaExtract: 1,
        purpleGelFoodColoring: 1
    },
    steps: ['Freeze the cake pan,', 'Cook half of the heavy cream with lavendar,', 'Cool the mixture and whip till firm peak,', 'Mix the rest of the ingredients,', 'Freeze again!'],
    serving: 4
};
let pantry = {
  heavyCream: 2,
  sweetenedCondensedMilk: 14,
  salt: 100,
  vanillaExtract: 5,
  iceCreamServing: 0
};

//Craving lavendar ice cream!
console.log('Craving lavendar ice cream!!!!');
if (pantry.iceCreamServing > 0) {
    console.log('Eat some ice cream.');
    pantry.iceCreamServing -= 1; //remember to decrease the servings of ice cream
    console.log('There\'re ' + pantry.iceCreamServing + ' serving(s) of ice cream left. Let\' make some!');
} 
else{
    console.log('Make ice cream!');
    makeCookies();

}

//fuction mixing(ingredients)

let makeCookies = () => {
    //check the pantry
    let ingredients = recipe.ingredients;
    // ingredients.test = true;
    // console.log(ingredients);
    // console.log(recipe.ingredients);
    for(let item in ingredients){
        let missingItem = !pantry[item];
        let notEnoughItem = pantry[item] <= ingredients[item];
        if(missingItem || notEnoughItem){
            pantry[item] = ingredients[item];
        }
    }
    //console.log(pantry);
    //console.log(ingredients);
    
    for(let item in ingredients){
        if(item !== 'iceCreamServing'){
            pantry[item] -= ingredients[item];
        }
    }
    pantry.iceCreamServing += recipe.serving;

    console.log("pantry: ");
    console.log(pantry);
    console.log("ingredients: ");
    console.log(ingredients);
}

/* oh no! There're no lavendar ice cream in the pantry!
In this exercise, using if else statements and loops to make cookies! Follow the sudo code!
*/

/*
if (there are lavendar ice cream) {
    eat a serving of lavendar ice cream
} else {
    1. check the pantry to see if you have enough ingredients
    hint: use loops and check the data type

    2. get all the missing ingredients
    hint: add to the ingredients in the pantry

    3. make lavendar ice cream!
    hint: subtract all the ingredients following the recipe
    hint 2: don't forget to add lavendar ice cream to the recipe, see 'serving' in recipe for number
}
*/

/*
    Bonus points: eat all the lavendar ice cream!
    hint: use a while loop
*/
