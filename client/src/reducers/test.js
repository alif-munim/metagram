import {TESTING} from '../action/type'

const initialState = {
    test_message: null
}

export default function(state = initialState, action ){
    const {type, payload} = action;

    switch(type){
        case TESTING:
            return{
                ...state,
                test_message: payload,
            }
        default:
            return state
    }
}