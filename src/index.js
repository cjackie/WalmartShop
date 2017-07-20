import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import Request from 'superagent';

class Shopping extends React.Component {
    constructor(props) {
    super(props);
    this.state = {
        groceries:[
        "albacoretuna",
        "bannas",
        "brownrice",
        "ceasardressing",
        "chickenthigh",
        "cottagecheese",
        "fujiapples",
        "greengrapes",
        "pintobeans",
        "raisenbread",
        "salad",
        "sarachasmall",
        "saraleebread",
        "smallshrimp",
        "spagettinoodles",
        "tomatoes",
        "wholegreekyogurt",
        "wholemilk",
        "wholetomatoes",
        "yellowonion"
    ]};
  }
  addtoCart(value) {
    console.log('ADDED', value)
    Request.get("http://127.0.0.1:5000/addtocart").query({item: value}).end(function (res) {
    if (res != null) {
      console.log('OK ', res)
    }
  });
  }

  removefromCart(value) {
    console.log('REMOVED',value)
    Request.get("http://127.0.0.1:5000/remove").query({item: value}).end(function (res) {
    if (res != null) {
      console.log('OK ', res)
    }
    });
  }

  render() {
    const listGroceries = this.state.groceries.map((item, i) => (
      <div className="col-md-3">
          <img src={'/src/images/' + item + '.jpg'}/>
          <button className="btn btn-success" onClick={() => this.addtoCart(item)}>Add to cart</button>
          <button className="btn btn-warning" onClick={() => this.removefromCart(item)}>Remove from cart</button>
      </div>
    ))

    return (
      <div>
        <div className="row">
          {listGroceries.slice(0,4)}
        </div>
        <div className="row">
          {listGroceries.slice(4,8)}
        </div>
        <div className="row">
          {listGroceries.slice(9,13)}
        </div>
        <div className="row">
          {listGroceries.slice(12,16)}
        </div>
      </div>
    );
  }
}

ReactDOM.render(<Shopping />, document.getElementById("root"));

