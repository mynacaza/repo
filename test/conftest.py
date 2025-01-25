import asyncpg

URL = "postgresql+asyncpg://postgres:111@localhost:5432/app_test"

CREATE_TABLES = """
CREATE TABLE users
(
id serial PRIMARY KEY,
email varchar(64),
hash_password varchar(255)
);

CREATE TABLE transactions 
(
id serial PRIMARY KEY,
operation_type varchar(50),
category_name varchar(50),
amount decimal,
comment text,
date date,
user_id int FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
)
"""

async def test_write_to_db_by_command():
  conn = await asyncpg.connect(URL)
  await conn.execute(CREATE_TABLES)
  await conn.commit()
  