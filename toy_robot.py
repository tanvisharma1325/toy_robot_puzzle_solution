from fastapi import FastAPI, HTTPException
app = FastAPI()

location = { "x-axis": 0, "y-axis": 0, "direction": "none"}

@app.get('/')
def landingPage(): 
    return {"message": "Welcome to toy-robot-puzzle please first use the place end point through http://127.0.0.1:8000/docs"}

@app.post("/place/")
def place(x: int, y: int, direction: str): 
    if not (0 <= x <= 4 and 0 <= y <= 4): 
        raise HTTPException(status_code=400, detail="Invalid position. Robot would fall off the table.") 
    if direction not in ["NORTH", "SOUTH", "EAST", "WEST"]: 
        raise HTTPException(status_code=400, detail="Invalid direction. Direction should be one of 'NORTH', 'SOUTH', 'EAST', 'WEST'.") 
    location["x-axis"] = x 
    location["y-axis"] = y 
    location["direction"] = direction 
    return location

@app.post("/left/")
def left(): 
    if location["direction"] == "EAST": 
        location["direction"] = "NORTH" 
    elif location["direction"] == "NORTH": 
        location["direction"] = "WEST" 
    elif location["direction"] == "WEST": 
        location["direction"] = "SOUTH" 
    elif location["direction"] == "SOUTH": 
        location["direction"] = "EAST" 

    return location

@app.post("/right/")
def right(): 
    if location["direction"] == "EAST": 
        location["direction"] = "SOUTH" 
    elif location["direction"] == "SOUTH": 
        location["direction"] = "WEST" 
    elif location["direction"] == "WEST": 
        location["direction"] = "NORTH" 
    elif location["direction"] == "NORTH": 
        location["direction"] = "EAST" 
    return location

@app.post("/move/")
def move(): 
    if location['direction'] == "none": 
        raise HTTPException(status_code=400, detail="The robot has not been placed on the table yet.") 
    
    if location['direction'] == "NORTH" and location["x-axis"] < 4: 
        location["x-axis"] += 1 
    elif location['direction'] == "SOUTH" and location["y-axis"] > 0: 
        location["y-axis"] -= 1 
    elif location['direction'] == "EAST" and location["y-axis"] < 4: 
        location["y-axis"] += 1 
    elif location['direction'] == "WEST" and location["x-axis"] > 0: 
        location["x-axis"] -= 1 
    else: 
        return {"x-axis": location["x-axis"], "y-axis": location["y-axis"], "direction": location["direction"], "message": 'This move is ignored'} 
    
    return location

@app.get("/report/")
def report(): 
    return location