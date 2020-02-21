import React, { Component } from 'react';
import './SearchAutoComplete.css';

class SearchAutoComplete extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div>
                <li className={this.props.typing ? "AutoComplete-list" : "AutoComplete-list-empty"}>
                    <ul>Really really really really long suggestion that no one cares about</ul>
                    <ul>Really really  long suggestion that no one cares about</ul>
                    <ul>Really really  really long suggestion that no one cares about</ul>
                    <ul>Really really really really long suggestion that no one cares about</ul>
                    <ul>Really really really long suggestion that no one cares about</ul>
                    <ul>Really really really really long suggestion that no one cares about</ul>
                    <ul>Really really really really long suggestion that no one cares about</ul>
                    <ul>Really really really long suggestion that no one cares about</ul>
                    <ul>Really really  really long suggestion that no one cares about</ul>
                    <ul>Really really really really long suggestion that no one cares about</ul>
                    <ul>Really really really long suggestion that no one cares about</ul>
                    <ul>....</ul>
                </li>
            </div>
        )
    }
}

export default SearchAutoComplete;