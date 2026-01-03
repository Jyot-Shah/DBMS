# Database Management System using Python & MySQL

A Python-based Employee Management System that connects to a MySQL database to manage various business operations.

## Features

- **Tasks Status** - View and manage task statuses
- **Sales Data** - Access monthly sales information
- **Company Branches Status** - Monitor branch performance
- **Salary & Attendance Details** - Track employee salary and attendance
- **Complains Management** - Handle customer complaints

## Prerequisites

- Python 3.x
- MySQL Server
- pip (Python package manager)

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/Jyot-Shah/DBMS.git
   cd DBMS
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   
   Create a `.env` file in the project root:
   ```env
   DB_HOST=localhost
   DB_USER=root
   DB_PASSWORD=your_password
   DB_NAME=your_DB_name
   ```

4. **Set up the database:**
   - Create a MySQL database
   - Import the required tables (tasks_status, sales_data, company_branches_status, salary_details, complains)

## Usage

Run the Main.py file:
```sh
python Main.py
```

## Project Structure

```
DBMS/
├── CEO_CTO.py              # CEO/CTO module with business operations
├── Member_Of_Staff.py      # Employee management module
├── Client.py               # Customer/Client module
├── Main.py                 # Application entry point
├── MainMenu.py             # Main menu navigation
├── Exit.py                 # Exit main menu function
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (not tracked in git)
├── LICENSE                 # License file
└── README.md               # Project documentation
```

## License

This project is licensed under the MIT License. Refer [LICENSE](LICENSE).

## Author

- [Jyot Shah](https://www.linkedin.com/in/jyotshah1/)
