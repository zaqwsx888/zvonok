from PostgresManager import PostgresManager

if __name__ == "__main__":
    db = PostgresManager()
    db.query(file_name='sql_query.sql', executescript=True)
    test_query = '''SELECT id FROM article
                WHERE id NOT IN (SELECT DISTINCT article_id FROM comment)'''
    result = db.query(test_query, fetchone=True)
    print(result)
