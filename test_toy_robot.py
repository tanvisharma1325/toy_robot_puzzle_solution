from fastapi.testclient import TestClient
from toy_robot import app 

client = TestClient(app)

def test_place():
    response = client.post("/place/?x=1&y=1&direction=NORTH")
    assert response.status_code == 200
    assert response.json() == {"x-axis": 1, "y-axis": 1, "direction": "NORTH"}

def test_left():
    client.post("/place/?x=1&y=1&direction=EAST")
    response = client.post("/left/")
    assert response.status_code == 200
    assert response.json() == {"x-axis": 1, "y-axis": 1, "direction": "NORTH"}

def test_right():
    client.post("/place/?x=1&y=1&direction=EAST")
    response = client.post("/right/")
    assert response.status_code == 200
    assert response.json() == {"x-axis": 1, "y-axis": 1, "direction": "SOUTH"}

def test_move():
    client.post("/place/?x=1&y=1&direction=NORTH")
    response = client.post("/move/")
    assert response.status_code == 200
    assert response.json() == {"x-axis": 2, "y-axis": 1, "direction": "NORTH"}

def test_report():
    client.post("/place/?x=1&y=1&direction=NORTH")
    response = client.get("/report/")
    assert response.status_code == 200
    assert response.json() == {"x-axis": 1, "y-axis": 1, "direction": "NORTH"}

def test_place_off_table():
    response = client.post("/place/?x=6&y=6&direction=NORTH")
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid position. Robot would fall off the table."}

def test_invalid_direction():
    response = client.post("/place/?x=1&y=1&direction=UPWARDS")
    assert response.status_code == 400
    assert response.json() == {"detail": "Invalid direction. Direction should be one of 'NORTH', 'SOUTH', 'EAST', 'WEST'."}

def test_move_off_table():
    client.post("/place/?x=0&y=0&direction=SOUTH")
    response = client.post("/move/")
    assert response.status_code == 200
    assert response.json() == {"x-axis": 0, "y-axis": 0, "direction": "SOUTH", "message": "This move is ignored"}

def test_move_before_place():
    client.post("/initialize/")
    response = client.post("/move/")
    assert response.status_code == 400
    assert response.json() == {"detail": "The robot has not been placed on the table yet."}