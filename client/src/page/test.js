import React from 'react'
import {connect} from 'react-redux'
import {tester} from '../action/testing'
import { useState } from 'react'
import { useEffect } from 'react'

const Test = ({test, tester}) => {
    const [value, setValue] = useState("")

    useEffect(() => {
        tester()
    },[])

    useEffect(() => {
        setValue(test.test_message)
    },[test.test_message])

    
    return (
        <div>
            test and {value}
        </div>
    )
}

const mapStateToProps = state => ({
    test: state.test
})

export default connect(mapStateToProps, {tester})(Test);
