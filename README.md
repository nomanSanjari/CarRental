# Car Rental

**Project Setup and Execution**

**Prerequisites:**

* Python 3.x installed ([https://www.python.org/downloads/](https://www.python.org/downloads/))
* Pip (Python package installer, usually included with Python)

**Project Structure:**

* **backend/**: Contains the Python source code for the FastAPI application.
    * **requirements.txt**: A list of required Python packages. 
    * **app.py** (or similar): Your main FastAPI application file.
    * **routers/**: Directory containing API route definitions.
    * **utils/**: Directory containing helper functions and modules.
* **database/**: Contains database-related files.
    * **main.sql**: The primary SQL file defining your database structure.
    * **database_dump.sql**: A database dump, possibly to provide initial data.
* **postman/**: Contains Postman collections.
    * **request_examples.json** (or similar): A Postman collection with sample request bodies.

**Setup Instructions:**

1. **Clone/Download the Project:** Obtain the project files from a repository (e.g., Git) or download them directly.
2. **Change Directory:** Open a terminal and navigate to the 'backend' folder of your project:
   ```bash
   cd backend
   pip install -r requirements.txt
   uvicorn main:app --reload
   ```
