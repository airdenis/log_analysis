import psycopg2
from text_format import TextFormat as TF


def most_popular_three_articles():
    try:
        db = psycopg2.connect("dbname=news")
        c = db.cursor()
        c.execute('''SELECT articles, count(*) AS num
                        FROM v_articles_authors_log
                        GROUP BY articles
                        ORDER BY num DESC
                        LIMIT 3;''')
        result = c.fetchall()
        db.close()
        print('{}Most popular three articles:{}'.format(''.join([TF.OKBLUE,
                                                                TF.UNDERLINE,
                                                                TF.BOLD]),
                                                        TF.END))
        for item in result:
            print("{} \"{}\" {} {} views".format(TF.BULLET,
                                                 item[0],
                                                 TF.EMDASH,
                                                 item[1]))
    except psycopg2.DatabaseError as error:
        print(''.join([TF.FAIL, TF.BOLD, str(error), TF.END]))
    finally:
        return


def most_popular_article_author():
    try:
        db = psycopg2.connect("dbname=news")
        c = db.cursor()
        c.execute('''SELECT authors, count(*) AS num
                        FROM v_articles_authors_log
                        GROUP BY authors
                        ORDER BY num DESC;''')
        result = c.fetchall()
        db.close()
        print('\n{}Most popular article author:{}'.format(''.join([TF.OKBLUE,
                                                                  TF.UNDERLINE,
                                                                  TF.BOLD]),
                                                          TF.END))
        for item in result:
            print("{} {} {} {} views".format(TF.BULLET,
                                             item[0],
                                             TF.EMDASH,
                                             item[1]))
    except psycopg2.DatabaseError as error:
        print(''.join([TF.FAIL, TF.BOLD, str(error), TF.END]))
    finally:
        return


def days_error():
    try:
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
        print('\n{}Days - more than 1% errors:{}'.format(''.join([TF.OKBLUE,
                                                                  TF.UNDERLINE,
                                                                  TF.BOLD]),
                                                         TF.END))
        for item in result:
            date_format = item[0].strftime("%d %B, %Y")
            print("{} {} {} {}% errors".format(TF.BULLET,
                                               date_format,
                                               TF.EMDASH,
                                               item[1]))

        print("{}{}Requests have been processed.{}".format(TF.OKGREEN,
                                                           TF.BOLD,
                                                           TF.END))
    except psycopg2.DatabaseError as error:
        print(''.join([TF.FAIL, TF.BOLD, str(error), TF.END]))
    finally:
        return


if __name__ == '__main__':
    most_popular_three_articles()
    most_popular_article_author()
    days_error()
