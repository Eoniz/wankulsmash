import os

# ********* IS DEBUG ********* 
DEBUG = True

# ********* BASE DIR ********* 
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# ********* SQLITE ***********
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
DATABASE_CONNECT_OPTIONS = {}

# ********* MAX THREADS ********* 
THREADS_PER_PAGE = 2

# ********* CSRF PART ********* 
CSRF_ENABLED = True
CSRF_SESSION_KEY = "{W;oB(&nxz.j_fWL#`_5XZ4*U[quO="

# ********* COOKIES SECURITY ********* 
SECRET_KEY = "GsQJ4x/'<>zf;e}]y=]LLwV^4in^s$"
