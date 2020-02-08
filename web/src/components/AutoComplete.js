import React from 'react'

export default class AutoComplete extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            items: [
                'Emmie',
                'Jasmine',
                'Varsha',
                'Catherine',
                'Abhinav',
                'Ved',
                'Andrew',
                'Abby',
                'Derrick',
                'Christopher'
            ],
            suggestions: []
        }
    }

    onAutoComplete = (s) => {
        return [];
    }

    onSearchChanged = (e) => {
        const val = e.target.value;
        let sug = [];
        if (val.length > 0) {
            const regex = new RegExp(`^${val}`, 'i')
            sug = this.state.items.sort().filter(v => regex.test(v))
            //const suggestions = this.onAutoComplete(val)
        }
        this.setState({
            suggestions: sug
        })
    }

    renderSuggestions() {
        const { suggestions } = this.state;
        if (suggestions.length === 0) {
            return null;
        }
        return (
            <ul>
                {suggestions.map((result) => <li>{result}</li>)}
            </ul>
        )
    }

    render() {
        return (
            <div>
                <input onChange={this.onSearchChanged} type='text'/>
                {this.renderSuggestions()}
            </div>
        )
    }
}