# before
def func_with_read_session(stmt: str):
    session = Session(read=True)
    session.excute(stmt)

def func_with_write_session(stmt: str):
    session = Session(write=True)
    session.excute(stmt)

func_with_write_session("INSERT INTO ...")
func_with_read_session("SELECT ...")


# after
def func_with_both_session(stmt: str, session: Session):
  session.execute(stmt)

read_session = Session(read=True)
write_session = Session(write=True)
func_with_both_session("INSERT INTO ...", write_session)
func_with_both_session("SELECT ...", read_session)
