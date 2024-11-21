import React from 'react'

const Row = ({Second, Sum, Color}) =>
{

    return  (
                <tr className="row">
                    <td style={{backgroundColor: Color}}>{`${Second}`}</td>
                    <td style={{backgroundColor: Color}}>{Sum}</td>
                </tr>
            )
}

export default Row