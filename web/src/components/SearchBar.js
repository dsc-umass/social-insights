import React, { Component } from 'react';
import './SearchBar.css';

class SearchBar extends Component {
    render() {
        return (
            <div className="search-bar">
                <input type="search" placeholder="Search here..." />
                <button type="submit" className="search-btn"><i class="fas fa-search"></i></button>
            </div>
        )
    }
}

export default SearchBar;