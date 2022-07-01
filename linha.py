def control (left_sensor, right_sensor, speed):
    L= left_sensor
    R= right_sensor
    P=1
    erro = R-L
    
    return{
        'engineTorque' : 3500,
        'brakingTorque': 1000,
        'steeringAngle': P*erro,
        'log':[
            {'name': 'Speed', 'value': speed, 'min':0, 'max':200},
            {'name': 'Left_sensor', 'value':L, 'min':0, 'max':1},  
            {'name': 'Right_sensor', 'value':R, 'min':0, 'max':1}
            ]
    }