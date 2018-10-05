import psycopg2


db = psycopg2.connect("dbname=news")
print('Connected to the database test table')
c = db.cursor()
c.execute('''SELECT articles, count(*) AS num
                FROM v_articles_authors_log
                GROUP BY articles
                ORDER BY num DESC
                LIMIT 3;''')
result = c.fetchall()
db.close()
for n in result:
    print(n)


db = psycopg2.connect("dbname=news")
print('Connected to the database test table')
c = db.cursor()
c.execute('''SELECT authors, count(*) AS num
                FROM v_articles_authors_log
                GROUP BY authors
                ORDER BY num DESC;''')
result = c.fetchall()
db.close()
for n in result:
    print(n)


db = psycopg2.connect("dbname=news")
print('Connected to the database test table')
c = db.cursor()
c.execute('''SELECT date, 
                    ROUND(COUNT(*) * 100::numeric/
                    (SELECT COUNT(*) FROM v_errors), 2) AS num
                FROM v_errors
                GROUP BY date
                ORDER BY num DESC
                LIMIT 1;''')
result = c.fetchall()
db.close()
for n in result:
    print(n)



