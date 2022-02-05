import axios from 'axios'
import {setAlert} from './alert'
import {
    TESTING
} from './type'

export const tester = () => async dispatch => {
    const config = {
        headers:{
            'Content-Type': 'application/json'
        }
    }
    try {
        const res = await axios.get('/test');
        dispatch({
            type: TESTING,
            payload: res.data
        })
        dispatch(setAlert("Testing", "andger"))

    } catch (error) {
        console.log(error)
    }
}