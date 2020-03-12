import React, { Component } from 'react';
import SearchResult from './SearchResult';
import {database} from './Database';
import './SearchAutoComplete.css'

class SearchAutoComplete extends Component {
    constructor(props) {
        super(props);
        this.handleResult = this.handleResult.bind(this);
    }

    handleResult(r) {
        this.props.onSelect(r);
    }

    render() {
        let filteredData = database.filter(
            (data) => {
                return data.toLowerCase().indexOf(this.props.query) != -1;
            }
        );

        return (
            <div>
                <ul className={this.props.typing ? "AutoComplete-list" : "AutoComplete-list-empty"}>
                    {filteredData.map(data => {
                        return <li><SearchResult result={data} getResult={this.handleResult}/></li>
                    })}
                </ul>
            </div>
        )
    }
}

export default SearchAutoComplete;