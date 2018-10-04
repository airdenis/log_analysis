import psycopg2


db = psycopg2.connect("dbname=news")
print('Connected to the database test table')
c = db.cursor()
c.execute('''select articles.title, count(*) as num from articles, log 
            where articles.slug=substring(log.path,10)
            group by articles.title
            order by num desc
            limit 3;''')
result = c.fetchall()
db.close()
for n in result:
    print(n)


db = psycopg2.connect("dbname=news")
print('Connected to the database test table')
c1 = db.cursor()
c1.execute('''select authors.name, count(*) as num from articles, log, authors 
            where articles.slug=substring(log.path,10) and articles.author=authors.id
            group by authors.name
            order by num desc;''')
result = c1.fetchall()
db.close()
for n in result:
    print(n)


db = psycopg2.connect("dbname=news")
print('Connected to the database test table')
c = db.cursor()
c.execute('''select time::timestamp::date, 
        round((count(time::timestamp::date)*100)::numeric
        / (select count(*) from log 
        where status != '200 OK'), 2)
        from log where status != '200 OK' 
        group by time::timestamp::date
        order by count(time::timestamp::date) desc
        limit 1;''')
result = c.fetchall()[0]
db.close()
print(result)

