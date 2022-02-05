import React from 'react'
import {connect} from 'react-redux'
import Alert from "@material-ui/lab/Alert"

const Alerts = ({alerts}) => 
    alerts !== null &&
    alerts.length > 0 &&
    alerts.map((alert) => (
        <div>
            <Alert severity="error">{alert.msg}</Alert>
        </div>
    ))
   

const mapStateToProps = (state) => ({
    alerts: state.alert,
})

export default connect(mapStateToProps)(Alerts)