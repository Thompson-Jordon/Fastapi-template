from contextlib import contextmanager
from app.db import Session
from app.testdb import Session as TestSession

# Dependency to get DB session.
def get_db():
    db = Session()
    try:
        yield db
    except:
        db.rollback()
        raise
    finally:
        db.close()


# Dependency to get DB session.
@contextmanager
def get_test_db():
    db = TestSession()
    try:
        yield db
    except:
        db.rollback()
        raise
    finally:
        db.close()