import React from 'react'
import {
    Link,
    Route,
} from 'react-router-dom'
import { render } from 'react-dom'

export default function Search() {
    return (
        <div align='center'>
            <input type='text' placeholder='Search...'></input>
            <button type='submit'><Link to='/results'>Enter</Link></button>
        </div>
    )
}