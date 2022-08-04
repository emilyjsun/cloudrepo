console.log('You have js connected');
// we're learning js today
//let x = 1 
//var y = 'Hello World!'; (difference with let is the scope)
    //with var can't use throughout the code
//const z = 'http://duke.edu';
    //can't change this



/*DataType exercise
In this exercise, we are going to create our own superhero character!
Remember to use console.log to help you debug*/

//First, declare an empty OBJECT variable called 'superhero'
let superhero = {superHeroName: 'QuickHands'};


/*Give the 'superhero' a first name, last name, superhero name, HP(hit points), 
3 stengthes in an ARRAY, 3 weaknesses in an ARRAY, a motto */

superhero.firstName = 'Deborah';
superhero.lastName = 'Jones';
superhero.HP = 100;
superhero.strength = ['Rock', 'Paper','Scissors'];
superhero.weakness = ['Paper', 'Scissors','Rock'];
//console.log(superhero);



//Set the superhero's alive status to true
let alive = superhero.HP > 0;
//console.log(typeof alive);


/*Now console.log to introduce the character using the 'superhero' OBJECT
For example, 'Hi, I'm Quick Hands. Fear me! 
My strenthes are Rock, Paper and Scissors. My weaknesses are Paper, Scissors and Rock.' */
let introductionOne = 'Hi, I\m ' + superhero.superHeroName + '. Fear me!';
let introductionTwo = `My strengths are ${superhero.strength[0]}, ${superhero.strength[1]}, and ${superhero.strength[2]}.`;
let introductionThree = `My weaknesses are ${superhero.weakness.join()}`;
//console.log(introductionOne);
//console.log(introductionTwo);
//console.log(introductionThree);


/*One day, the superhero is on the way to rescue a kitten on the tree, a monster shows up to fight.
Create 4 BOOLEAN variables: hero, monster, hit, miss, and assign them the correct value so that:
superhero and monster cannot both win; either superhero or monster wins;
superhero always hits and never miss; 
monster always misses and never hit.
At the end, console.log superhero's victory.*/
let superHero = true;
let monster = false;
let hit = true;
let miss = false;
//console.log('Superhero and monster cannot both win? ' + (superHero && monster));
//console.log('Either superhero or monster wins? ' + (superHero || monster));
//console.log('Superhero never miss? ' + (superHero && miss));




/*The superhero trips over a cardboard box, and loses half of the HP,
loses all the strengthes and gains a weakness: cardboard box.
console.log the new superhero status and make sure the hero is still alive.*/
superhero.HP = superhero.HP/2;
superhero.weakness.push('Cardboard Box');
console.log(superhero.weakness);
superhero.strength = [];
console.log(superhero.strength);
alive=  superhero.HP > 0;
console.log(alive);


/*BONUS: create a monster character. 
Give both the monster and the hero attack and defense value. 
Now let them battle till the end. The hero might die this time ;(
*/
