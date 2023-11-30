
#https://stackoverflow.com/questions/5010042/mysql-get-column-name-or-alias-from-query
def format_row_to_dict(cursor):
  fields = [field_md[0] for field_md in cursor.description]
  result = [dict(zip(fields,row)) for row in cursor.fetchall()]

  return result