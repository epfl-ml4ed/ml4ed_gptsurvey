# Backend API

**An example FastAPI backkend is available in `utils/backend_example.py`**

## Database

You are free to store your data with your prefered system. Here we will represent the data as a simple dict, indexed by courseID -> studentID :

```json
course_data = {
    "CS-401" : {
        "000000" : student_course_data,
        "000001" : student_course_data,
        etc.
    }
    "MATH-101": {
        "123456" : student_course_data,
        "111111" : student_course_data,
        etc.
    }
    etc.
}
```

`student_course_data` which is `courses_data[courseID][studentID]` has the following structure :

```json
{
    "TaskName":"Quiz 1: Exercise 8",
    "TaskBody":"Let $x$ be a real number. Prove that if $x^2$ is etc.",
    "TaskSolutionBody":"x is rationnal premise x = p/q with etc.",
    "AIFeedback": "Your understanding of the concepts is evident, but etc.",
    "HumanFeedback": "You got the correct assumption, but etc."
    
}
```

The strings support markdown format. This can be used to create rich text with links, embedded images, bullet points, math formulas, etc.

# Methods

The frontend expects the following GET / POST methods to exist in the backend :

## gather_data (GET)

```python
@router.get("/ml4ed_survey/gather_data")
def gather_data(sciperID: str, courseID: str) -> dict:
    """Returns all the data necessary for the survey."""

    # Raise 400 error if invalid arguments
    # ...
    # Then :
    return courses_data[courseID][sciperID]
```

## write_results (POST)

```python
@router.post("/ml4ed_survey/write_results")
def write_results(data: dict):
    """Saves the survey result, the request body will be a json containing `SciperID` and `CourseID`."""

    courseID = data["CourseID"]
    sciperID = data["SciperID"]
    write_to_storage(f"result_{courseID}_{sciperID}.json", data)
    return "ok (logs saved)"
```

You are free to implement the `write_to_storage` to store it on your storage system (S3 bucket, DB, etc.)

## list_courses (GET)

```python
@router.get("/ml4ed_survey/list_courses")
def list_courses():
    """Returns courses description. `id` should correspond to a valid courseID in the database."""

    courses_description = [
        {
            "id": "BIO-210",
            "text": "BIO-210: Applied software engineering for life sciences",
        },
        {
            "id": "CS-101",
            "text": "CS-101: Advanced information, computation, communication",
        },
        etc.
    ]
    return courses_description
```