import React from 'react'
import Row from './row';
import { useFetch } from '../scripts/fetch';

const Body = () =>
{
    const Data = useFetch()
    const Elements = []
    for (const [key, value] of Object.entries(Data))
    {
        if (value[0] != 0)
        {
            Elements.push(<Row Second={key} Sum={value[0]} Color={value[1]}/>)
        }
    }

    return  Data !== "stop" ? <tbody>
                    {Elements}
                </tbody> : <div>Program on hold, too much memory being used.</div>

}

export default Body
