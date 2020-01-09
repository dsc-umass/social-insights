import React from 'react'

export default function Results(props) {
    return (
        <div>
            <h3>Results for '{props.search}'</h3>
            <ul>
                {props.list.map((result) => (
                    <li key={result.url}>
                        <a href='result.url'>{result.header}</a>
                    </li>
                ))}
            </ul>
        </div>
    )
}
