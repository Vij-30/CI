from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Dict
import csv

app = FastAPI()

# Enable CORS to allow GET requests from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_methods=["GET"],  # Only allow GET requests
    allow_headers=["*"],   # Allow all headers
)

# Read the CSV file once when the server starts
students_data: List[Dict[str, str]] = []

with open("q-fastapi.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        row["studentId"] = int(row["studentId"])  # Ensure studentId is int
        students_data.append(row)

# API endpoint
@app.get("/api")
async def get_students(class_: List[str] = []):
    if class_:
        filtered = [student for student in students_data if student["class"] in class_]
        return {"students": filtered}
    return {"students": students_data}
