import React, { Component } from 'react';

class SearchResult extends Component {
    constructor(props) {
        super(props);
        this.sendResult = this.sendResult.bind(this);
    }

    sendResult() {
        this.props.getResult(this.props.result);
    }

    render() {
        return (
            <div onClick={this.sendResult}>
                {this.props.result}
            </div>
        )
    }
}

export default SearchResult;