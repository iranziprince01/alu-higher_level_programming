<h1 font-weight="Bold">Python - Object-relational mapping<h1>
<h1 font-weight="bold">Before you start...</h1>
<p><strong>Please make sure your MySQL server is in 8.0</strong></p>
<h2 font-weight="Bold"> Background context</h2>
<p>In this project, you will link two amazing worlds: Databases and Python!</p>
<p>In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.</p>
<p>In the second part, you will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).</p>
<p>The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage.</p> 
<p>With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”.</p> 
<p>You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent.</p> 
<p>You will be able to change your storage easily without re-writing your entire project.</p>
Without ORM:
<div>conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()</div>
With ORM:
<div>engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()</div>
<h2>Resources</h2>
Read or Watch:
<li><a href="https://www.fullstackpython.com/object-relational-mappers-orms.html">Object-relational mappers</a>(until “26.2.3.7. Warnings” included)</li>
<li><a href="https://mysqlclient.readthedocs.io/">mysqlclient/MySQLdb documentation</a></li>
<li><a href="https://www.mikusa.com/python-mysql-docs/index.html">MySQLdb tutorial</a></li>
<li><a href="https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/">SQLAlchemy ORM Tutorial for Python Developers</a></li>
<li><a href="http://alextechrants.blogspot.com/2013/11/10-common-stumbling-blocks-for.html">10 common stumbling blocks for SQLAlchemy newbies</a></li>
<li><a href="https://docs.sqlalchemy.org/en/13/orm/tutorial.html">SQLAlchemy tutorial</a></li>
</ul>
<h2 font-weight="Bold">Learning Objectives</h2>
<p>At the end of this project, you are expected to be able to <a href="https://fs.blog/feynman-learning-technique/">explain to anyone</a>, <strong>without the help of Google</strong>:</p>
<h3>General</h3>
<ul>
<li>Why Python programming is awesome</li>
<li>How to connect to a MySQL database from a Python script</li>
<li>How to SELECT rows in a MySQL table from a Python script</li>
<li>How to INSERT rows in a MySQL table from a Python script</li>
<li>What ORM means</li>
<li>How to map a Python Class to a MySQL table</li>
</ul>
