//import logo from './logo.svg';
import './App.css';
//import Item from './MyItem';
import React from 'react';

class FilmItemRow extends React.Component{
  render(){
    return(
      <li>
        <a href={this.props.url}>{this.props.url}</a>
      </li>
    )
  }
}
class StarWars extends React.Component{
  constructor(){
    super()
    this.state={
      name:null,
      height:null,
      homeworld:null,
      image:null,
      films:[],
      loadedCharacter:false
    }
  }
  getNewCharacter(){
    const num=Math.round((Math.random()*82));
    const url=`https://rawcdn.githack.com/akabab/starwars-api/0.2.1/api/id/${num}.json`;
    fetch(url)
    .then(response => response.json())
    .then(data=> {
      this.setState({
      name:data.name,
      height:data.height,
      homeworld:data.homeworld,
      films:data.films,
      image: data.image,
      loadedCharacter:true
    })})
  }
  render(){
    //const movies=this.state.films.map((url,i) => {return <FilmItemRow key={i} url={url}/>})
    return(
      <div>
        {
          this.state.loadedCharacter &&
          <div>
            <img src={this.state.image} alt="" width='200px'></img>
            <h1>{this.state.name}</h1>
            <p>{this.state.height}cm</p>
            <p><a href={this.state.homeworld}>Homeworld</a></p> 
          </div>
        }
        <button type="button" onClick={()=> this.getNewCharacter()} class="btn"> Randomise Character</button>
      </div>
    )
  }
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <StarWars/>
      </header>
    </div>
  );
}

export default App;
