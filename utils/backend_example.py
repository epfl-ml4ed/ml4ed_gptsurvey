from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


courses_data = {
    "CS-401": {
        "000000": {
            "TaskName": "Quiz 1: Exercise 8",
            "TaskBody": "Let $x$ be a real number. Prove that if $x^2$ is etc.",
            "TaskSolutionBody": "x is rationnal premise x = p/q with etc.",
            "AIFeedback": "Your understanding of the concepts is evident, but etc.",
            "HumanFeedback": "You got the correct assumption, but etc.",
        },
        "000001": {
            "TaskName": "Quiz 1: Exercise 8",
            "TaskBody": "Let $x$ be a real number. Prove that if $x^2$ is etc.",
            "TaskSolutionBody": "To prove this we should first etc.",
            "AIFeedback": "This is a great explanation, but etc.",
            "HumanFeedback": "You have well understood that etc.",
        },
    },
    "MATH-101": {
        "123456": {
            "TaskName": "Midterm Exam : Exercise II",
            "TaskBody": "Given the dot product of $A$ and $B$ with etc.",
            "TaskSolutionBody": "To prove the statement we should first take $A$ and etc.",
            "AIFeedback": "The first part is correct, but in the second part etc.",
            "HumanFeedback": "You have made a mistake in the second part, the etc.",
        },
        "111111": {
            "TaskName": "Midterm Exam : Exercise II",
            "TaskBody": "Given the dot product of $A$ and $B$ with etc.",
            "TaskSolutionBody": "To show this, let's fist take $B$ and etc.",
            "AIFeedback": "Great ! The proof is correct, but etc.",
            "HumanFeedback": "The proof is correct, but you should etc.",
        },
    },
}

courses_description = [
    {
        "id": "CS-401",
        "text": "CS-401: Advanced information, computation, communication",
    },
    {
        "id": "MATH-101",
        "text": "MATH-101: Introduction to Calculus",
    },
]


@app.get("/ml4ed_survey/gather_data")
def gather_data(sciperID: str, courseID: str):
    """Returns all the data necessary for the survey."""
    if courseID in courses_data:
        if sciperID in courses_data[courseID]:
            return courses_data[courseID][sciperID]
        raise HTTPException(
            status_code=400,
            detail=f"Sciper not found in {courseID}, make sure you indicated the correct course. Contact support otherwise.",
        )
    raise HTTPException(status_code=400, detail="Invalid courseID, contact support.")


@app.post("/ml4ed_survey/write_results")
def write_results(data: dict):
    """Saves the survey result, the request body will be a json containing `SciperID` and `CourseID`."""

    courseID = data["CourseID"]
    sciperID = data["SciperID"]
    print(f"Received results for {sciperID} in {courseID} with the following content :")
    print(data)
    print("This only is a dummy backend example that prints the data.")
    print("In production this should store to your database.")
    return "ok (logs saved)"


@app.get("/ml4ed_survey/list_courses")
def list_courses():
    """Returns courses description. `id` should correspond to a valid courseID in the database."""
    return courses_description
