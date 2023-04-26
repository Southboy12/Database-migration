GoFrieghts World Port Index Migration
The World Port Index is a comprehensive database of ports and terminals around the world, containing information about their physical characteristics, facilities, and services. As part of our work at GoFrieghts, we have migrated this data from an old Access database to a modern PostgreSQL database, and created data marts by analyzing the data.

Prerequisites:

Python 3.6 or later
PostgreSQL 10 or later
psycopg2
dotenv
sqlachelmy
opendatasets
pandas

Installation:

1. Clone the repository:

```python copyable
https://github.com/Southboy12/Database-migration.git
```

2. Create a virtual environment and activate it:

```python copyable
python3 -m venv venv
source venv/bin/activate
```

3. Install the requirements:

```python copyable
pip install -r requirements.txt
```

Usage:

To migrate the World Port Index data from Access database to Postgres, run the following command:

```python copyable
pythonn script.py
```

To create the tables for the three questions, run the following commands

```python copyable
python nearest_ports_table.py
python largest_port_count_table.py
python nearest_port_with_provisions_table.py


Extract Load (EL) Pipeline

We have built an Extract Load (EL) pipeline to migrate the World Port Index data from the old Access database to out PostgreSQL database. The Access database can be accessed through the following link:

```python copyable
https://drive.google.com/file/d/1VyCGCAfFuEK7vB1C9Vq8iPdgBdu-LDM4/view?usp=share_link
```

Contributing:

Contributions are welcome! Please feel free to open an issue or pull request if you have any suggestions or improvements.

License:

This project is licensed under the MIT License.