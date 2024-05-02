from fastapi import FastAPI 


app  = FastAPI() ; 

@app.get('/get-weather')
async def get_weather():
    return {'data' : {
        'city' : 'Bengaluru' , 
        'Temperature' : 34 , 
        'Scale' : 'Celsius'
    }}