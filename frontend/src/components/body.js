import React from 'react'
import Row from './row';
import { useFetch } from '../scripts/fetch';

const Body = () =>
{
    const Data = useFetch()["Data"]

    return  <tbody>{
            Data ? Data.map((Entry) =>
            {
                return <Row Second={Entry["_id"]["datetime"]} Sum={Entry["sum"]} Color={Entry["color"]}/>
            }) : <div>No data</div>}
            </tbody>
}

export default Body
