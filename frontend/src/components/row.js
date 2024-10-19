import React from 'react'

const Row = ({Second, Sum, Color}) =>
{
    const r = Color[0]
    const g = Color[1]
    const b = Color[2]
    const RGB = `rgb(${r}, ${g}, ${b})`

    return  (
                <tr className="row">
                    <td style={{backgroundColor: RGB}}>{`${Second}`}</td>
                    <td style={{backgroundColor: RGB}}>{Sum}</td>
                </tr>
            )
}

export default Row