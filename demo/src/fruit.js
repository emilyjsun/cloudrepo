import logo from './logo.svg';
import './App.css';
import React from 'react';

export function Fruit(props) {
    let fruit = {
        name: props.fruit,
        color: 'red',
        quantity: 1
    };
    const fruitColor = 
        <>
            <p>The color is {fruit.color}.</p>
            <p>{fruit.name} is good. </p>
            
        </>
    return (
        <div>
            <h1>This is a fruit</h1>
            {fruitColor}
            <button onClick={() => props.changeFruit('Banana')}>change fruit</button>
            
        </div>
    );
}



export default Fruit;
