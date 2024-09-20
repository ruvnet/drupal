# Migration Guide

This document provides detailed instructions on how to migrate data and templates from the existing Drupal implementation to the new Python-based implementation using FastAPI, Pydantic, and SQLAlchemy.

## Prerequisites

Before starting the migration process, ensure that you have the following tools and dependencies installed:

- Python 3.8 or higher
- FastAPI
- Pydantic
- SQLAlchemy
- Alembic (for database migrations)
- PostgreSQL (or your preferred database)
- Docker (optional, for containerized deployment)

## Step-by-Step Migration Process

### 1. Set Up the Development Environment

1. Clone the repository and navigate to the project directory:

   ```sh
   git clone https://github.com/your-repo/drupal-python.git
   cd drupal-python
   ```

2. Create a virtual environment and activate it:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies using Poetry:

   ```sh
   poetry install
   ```

   Alternatively, you can use `pip` and `setup.py`:

   ```sh
   pip install -r requirements.txt
   ```

### 2. Database Migration

1. Export the existing Drupal database to a SQL file:

   ```sh
   drush sql-dump > drupal_database.sql
   ```

2. Create a new PostgreSQL database for the Python implementation:

   ```sh
   createdb drupal_python
   ```

3. Import the exported Drupal database into the new PostgreSQL database:

   ```sh
   psql drupal_python < drupal_database.sql
   ```

4. Use Alembic to generate and apply database migrations for the new schema:

   ```sh
   alembic revision --autogenerate -m "Initial migration"
   alembic upgrade head
   ```

### 3. Data Transformation

1. Write a script to transform the data from the Drupal schema to the new schema. This may involve:

   - Mapping Drupal content types to FastAPI models
   - Converting Drupal field data to Pydantic models
   - Updating relationships and foreign keys

   Example script:

   ```python
   from sqlalchemy import create_engine
   from sqlalchemy.orm import sessionmaker
   from drupal_python.models import Base, NewModel
   from drupal_python.schemas import NewModelSchema

   engine = create_engine('postgresql://user:password@localhost/drupal_python')
   Session = sessionmaker(bind=engine)
   session = Session()

   # Example transformation
   old_data = session.execute("SELECT * FROM drupal_table").fetchall()
   for row in old_data:
       new_data = NewModelSchema(
           field1=row['old_field1'],
           field2=row['old_field2'],
           # Add more field mappings as needed
       )
       new_model = NewModel(**new_data.dict())
       session.add(new_model)

   session.commit()
   ```

### 4. Template Migration

1. Identify the templates used in the existing Drupal implementation.

2. Convert the Drupal templates to Jinja2 templates for use with FastAPI.

3. Update the FastAPI routes to render the new Jinja2 templates.

   Example route:

   ```python
   from fastapi import FastAPI, Request
   from fastapi.templating import Jinja2Templates

   app = FastAPI()
   templates = Jinja2Templates(directory="templates")

   @app.get("/")
   async def read_root(request: Request):
       return templates.TemplateResponse("index.html", {"request": request})
   ```

### 5. Testing and Validation

1. Test the new implementation to ensure that all data has been migrated correctly and that the application functions as expected.

2. Validate the data integrity and consistency between the old and new implementations.

3. Perform user acceptance testing (UAT) to ensure that the new implementation meets the requirements.

## Tools and Scripts

- [Alembic](https://alembic.sqlalchemy.org/) - Database migration tool for SQLAlchemy.
- [Jinja2](https://jinja.palletsprojects.com/) - Templating engine for Python.
- [Drush](https://www.drush.org/) - Command-line shell for Drupal.

## Conclusion

By following this migration guide, you should be able to successfully migrate your existing Drupal implementation to the new Python-based implementation using FastAPI, Pydantic, and SQLAlchemy. If you encounter any issues or have questions, please refer to the project documentation or seek assistance from the development team.
