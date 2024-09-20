# Database Setup and Instructions

This document provides SQL scripts and instructions for setting up the database, including instructions for using Supabase, describing the database schema and relationships, and providing information on database migrations and versioning.

## SQL Scripts

### Create Tables

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL
);

CREATE TABLE contents (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    body TEXT NOT NULL,
    author_id INTEGER REFERENCES users(id)
);
```

### Insert Sample Data

```sql
INSERT INTO users (username, email, hashed_password) VALUES
('john_doe', 'john@example.com', 'hashed_password_1'),
('jane_doe', 'jane@example.com', 'hashed_password_2');

INSERT INTO contents (title, body, author_id) VALUES
('First Post', 'This is the body of the first post.', 1),
('Second Post', 'This is the body of the second post.', 2);
```

## Instructions for Using Supabase

Supabase is an open-source Firebase alternative that provides a suite of tools for building and managing databases. Follow these steps to set up and use Supabase for this project:

1. **Sign Up and Create a Project:**
   - Go to [Supabase](https://supabase.io/) and sign up for an account.
   - Create a new project and note down the project URL and API key.

2. **Set Up the Database:**
   - Go to the "Database" section of your Supabase project.
   - Run the SQL scripts provided above to create the tables and insert sample data.

3. **Configure the Application:**
   - Update the `DATABASE_URL` environment variable in your application to use the Supabase database URL.
   - Example:
     ```bash
     export DATABASE_URL="postgresql://<DB_USER>:<DB_PASSWORD>@<SUPABASE_URL>/<DB_NAME>"
     ```

4. **Use Supabase Client Libraries:**
   - Supabase provides client libraries for various languages and frameworks. Use the appropriate client library to interact with the Supabase database from your application.
   - Example (using JavaScript):
     ```javascript
     import { createClient } from '@supabase/supabase-js';

     const supabaseUrl = 'https://<SUPABASE_URL>';
     const supabaseKey = '<SUPABASE_KEY>';
     const supabase = createClient(supabaseUrl, supabaseKey);

     // Example query
     const { data, error } = await supabase
       .from('users')
       .select('*');
     ```

## Database Schema and Relationships

The database schema consists of two main tables: `users` and `contents`. The `users` table stores user information, while the `contents` table stores content created by users. The `author_id` column in the `contents` table references the `id` column in the `users` table, establishing a relationship between the two tables.

### Users Table

- **id**: Primary key, unique identifier for each user.
- **username**: Unique username for each user.
- **email**: Unique email address for each user.
- **hashed_password**: Hashed password for each user.

### Contents Table

- **id**: Primary key, unique identifier for each content item.
- **title**: Title of the content.
- **body**: Body of the content.
- **author_id**: Foreign key referencing the `id` column in the `users` table.

## Database Migrations and Versioning

Database migrations are managed using Alembic, a lightweight database migration tool for SQLAlchemy. Follow these steps to create and apply database migrations:

1. **Initialize Alembic:**
   - Run the following command to initialize Alembic in your project:
     ```bash
     alembic init alembic
     ```

2. **Configure Alembic:**
   - Update the `alembic.ini` file with your database URL:
     ```ini
     sqlalchemy.url = postgresql://<DB_USER>:<DB_PASSWORD>@localhost/<DB_NAME>
     ```

3. **Create a Migration Script:**
   - Run the following command to create a new migration script:
     ```bash
     alembic revision --autogenerate -m "Initial migration"
     ```

4. **Apply the Migration:**
   - Run the following command to apply the migration to the database:
     ```bash
     alembic upgrade head
     ```

5. **Manage Migrations:**
   - Use the following commands to manage database migrations:
     - **Create a new migration**: `alembic revision --autogenerate -m "Migration message"`
     - **Apply migrations**: `alembic upgrade head`
     - **Revert migrations**: `alembic downgrade -1`

By following these instructions, you can set up and manage the database for the project, including using Supabase, understanding the database schema and relationships, and managing database migrations and versioning.
