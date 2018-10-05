from time import strftime
import psycopg2


def most_popular_three_articles():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute('''SELECT articles, count(*) AS num
                    FROM v_articles_authors_log
                    GROUP BY articles
                    ORDER BY num DESC
                    LIMIT 3;''')
    result = c.fetchall()
    db.close()
    
    print('\033[4m\033[1m\033[93m' + 
            "The most popular three articles of all time are:" +
            '\033[0m')

    for item in result:
        print(u"\u2022 \"{}\" \u2014 {} views".format(*item))

    print("\n")
    return


def most_popular_article_author():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute('''SELECT authors, count(*) AS num
                    FROM v_articles_authors_log
                    GROUP BY authors
                    ORDER BY num DESC;''')
    result = c.fetchall()
    db.close()

    print('\033[4m\033[1m\033[93m' +
            "The most popular article authors of all time are:" +
            '\033[0m')

    for item in result:
        print(u"\u2022 \"{}\" \u2014 {} views".format(*item))

    print("\n")
    return


def days_error():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute('''
                SELECT date, 
                        ROUND(COUNT(*) * 100::numeric/
                        (SELECT COUNT(*) FROM v_errors), 2) AS num
                    FROM v_errors
                    GROUP BY date
                    HAVING 
                        ROUND(COUNT(*) * 100::numeric/
                        (SELECT COUNT(*) FROM v_errors), 2) > 1
                    ORDER BY num DESC;''')
    result = c.fetchall()
    db.close()

    print('\033[4m\033[1m\033[93m' +
            "Days which more than 1% of error requests are:" +
            '\033[0m')
    
    for item in result:
        date_format = item[0].strftime("%d %B, %Y")

        print(u"\u2022 {} \u2014 {}% errors".format(date_format, item[1]),)
    print("Requests have been processed.")
    return


if __name__ == '__main__':
    most_popular_three_articles()
    most_popular_article_author()
    days_error()
