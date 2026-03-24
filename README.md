# DevTrack

A minimal Django backend API for tracking engineering issues.

## How to Run

1. Open your terminal and navigate into the project folder: `cd devtrack`
2. Activate the virtual environment (if you are using one): `source venv/bin/activate` 
3. Start the server: `python manage.py runserver`
4. Test the API locally! Open Postman and try testing specific endpoints directly, such as:
   - `http://127.0.0.1:8000/api/issues/`
   - `http://127.0.0.1:8000/api/reporters/`

## Endpoints

**Reporters:**
- `POST /api/reporters/` - Create a reporter
- `GET /api/reporters/` - Get all reporters
- `GET /api/reporters/?id=1` - Get reporter by ID

**Issues:**
- `POST /api/issues/` - Create an issue
- `GET /api/issues/` - Get all issues
- `GET /api/issues/?id=1` - Get issue by ID
- `GET /api/issues/?status=open` - Get filtered issues

## Design Decision

**Decision:** We stored data in simple JSON files instead of setting up a database.  
**Why:** The assignment specifically asked us to build our own Python classes from scratch (`BaseEntity`, `Reporter`, `Issue`). If we used a Django database, Django would have forced us to use its own pre-made classes instead of letting us write our own!

## Testing Screenshots

### Success Scenarios (Status 200/201)
- ![Success 1](postman_screenshots/success/Screenshot%202026-03-24%20at%2021.39.35.png)
- ![Success 2](postman_screenshots/success/Screenshot%202026-03-24%20at%2021.39.52.png)
- ![Success 3](postman_screenshots/success/Screenshot%202026-03-24%20at%2021.40.39.png)
- ![Success 4](postman_screenshots/success/Screenshot%202026-03-24%20at%2021.41.18.png)
- ![Success 5](postman_screenshots/success/Screenshot%202026-03-24%20at%2021.41.36.png)
- ![Success 6](postman_screenshots/success/Screenshot%202026-03-24%20at%2021.41.45.png)
- ![Success 7](postman_screenshots/success/Screenshot%202026-03-24%20at%2021.42.22.png)

### Failure Scenarios (Status 400/404)
- ![Failure 1](postman_screenshots/failure/Screenshot%202026-03-24%20at%2021.45.23.png)
- ![Failure 2](postman_screenshots/failure/Screenshot%202026-03-24%20at%2021.46.41.png)
- ![Failure 3](postman_screenshots/failure/Screenshot%202026-03-24%20at%2021.47.59.png)
