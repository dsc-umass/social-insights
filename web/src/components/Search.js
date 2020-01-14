import React from 'react'
import {
    Link,
    Route,
} from 'react-router-dom'
import Results from './Results'
import { render } from 'react-dom'

export default class Search extends React.Component{
    constructor(props) {
        super(props)

        this.state = {
            results: [
                {
                    url: 'google.com',
                    header: 'Source 1'
                },
                {
                    url: 'youtube.com',
                    header: 'Source 2'
                },
                {
                    url: 'github.com',
                    header: 'Source 3'
                },
                {
                    url: 'instagram.com',
                    header: 'Source 4'
                }
            ],
            input: '',
            loading: false
        }

        this.updateInput = this.updateInput.bind(this)
        this.fetchResults = this.fetchResults.bind(this)
        this.refresh = this.refresh.bind(this)
    }

    fetchResults() {
        return this.state.results;
    }

    updateInput(e) {
        const value = e.target.value
        this.setState(() => ({
            input: value
        }))
    }

    refresh() {

    }

    render() {
        return (
            <div align='center'>
                <input
                    type='text'
                    placeholder='Search...'
                    value={this.state.input}
                    onChange={this.updateInput}
                />  
                <button type='submit'><Link to='/results'>Enter</Link></button>
                <Results 
                    list={this.state.results}
                    search={this.state.input}
                />
            </div>
        )
    }
}