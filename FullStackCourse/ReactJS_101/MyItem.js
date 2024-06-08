import React from "react";
class Item extends React.Component{
    constructor(props){
        super(props)
        this.state={
            clicks :0,
            totalRemaining: 100,
        }
    }
    clickMe(){
        this.setState({
            clicks : this.state.clicks + 1,
            totalRemaining: this.state.totalRemaining-1
        })
        console.log("I was clicked:", this.props.name)
    }
    render(){
      return(
        <div>
        <h1 onClick={()=>this.clickMe()} >Hello World from {this.props.name}</h1>
        <span>{this.state.clicks} is the number of clicks.{this.state.totalRemaining}</span>
      </div>
      )
    }
}

export default Item;