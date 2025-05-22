import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    mapper = {'id' : 'student_id', 'first' : 'first_name', 'last' : 'last_name', 'age' : 'age_in_years'}
    students = students.rename(columns = mapper)
    return students
    