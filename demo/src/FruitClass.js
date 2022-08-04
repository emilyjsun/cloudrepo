class FruitClass extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            fruit: {
                name: this.props.fruit,
                color: 'red',
                quantity: 1
            },
            anni: 'cat'
        }
    }


    handleClick = () =>{
        this.setState({anni:'dog'});
    }

    renderAnimal = () => {
        if(this.state.anni === 'cat'){
            return <h3>cat</h3>
        }
        else{
            return <h3>dog</h3>
        }
    }

    render(){
        const fruitColor = 
        <>
            <p>The color is {this.state.fruit.color}.</p>
            <p>{this.state.fruit.name} is good. </p>
            
        </>
    return (
        <div>
            <h1>This is a fruit</h1>
            {this.renderAnimal()}
            {/* {fruitColor} */}
            <button onClick={this.handleClick}>change animal</button>
        </div>
    );
    }
    

}