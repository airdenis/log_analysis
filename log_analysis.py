#!/usr/bin/python3
import psycopg2
from text_format import TextFormat


def most_popular_three_articles():
    try:
        db = psycopg2.connect("dbname=news")
        c = db.cursor()
        c.execute('''SELECT articles, count(*) AS num
                        FROM v_articles_authors_log
                        GROUP BY articles
                        ORDER BY num DESC
                        LIMIT 3;''')
        results = c.fetchall()
        db.close()
        print(
            '{}Most popular three articles:{}'.format(
                ''.join(
                    [TextFormat.OKBLUE, TextFormat.UNDERLINE, TextFormat.BOLD]
                ),
                TextFormat.END
            )
        )

        for (article, views) in results:
            print(
                "{} \"{}\" {} {} views".format(
                    TextFormat.BULLET,
                    article,
                    TextFormat.EMDASH,
                    views
                )
            )

    except psycopg2.DatabaseError as error:
        print(
            ''.join(
                [TextFormat.FAIL, TextFormat.BOLD, str(error), TextFormat.END]
            )
        )

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
        results = c.fetchall()
        db.close()

        print(
            '\n{}Most popular article author:{}'.format(
                ''.join(
                    [TextFormat.OKBLUE, TextFormat.UNDERLINE, TextFormat.BOLD]
                ),
                TextFormat.END
            )
        )

        for (author, views) in results:
            print(
                "{} {} {} {} views".format(
                    TextFormat.BULLET,
                    author,
                    TextFormat.EMDASH,
                    views
                )
            )

    except psycopg2.DatabaseError as error:
        print(
            ''.join(
                [TextFormat.FAIL, TextFormat.BOLD, str(error), TextFormat.END]
            )
        )

    finally:
        return


def days_error():
    try:
        db = psycopg2.connect("dbname=news")
        c = db.cursor()
        c.execute('''
                SELECT v_errors.date,
                  ROUND(
                    (v_errors.errors_count/v_total.total_count::NUMERIC) * 100,
                        2)
                FROM v_errors, v_total
                WHERE v_errors.date = v_total.date and
                  v_errors.errors_count/v_total.total_count::NUMERIC>0.01;''')
        results = c.fetchall()
        db.close()

        print(
            '\n{}Days - more than 1% errors:{}'.format(
                ''.join(
                    [TextFormat.OKBLUE, TextFormat.UNDERLINE, TextFormat.BOLD]
                ),
                TextFormat.END
            )
        )

        for (date, percent) in results:
            date_format = date.strftime("%d %B, %Y")
            print(
                "{} {} {} {}% errors".format(
                    TextFormat.BULLET,
                    date_format,
                    TextFormat.EMDASH,
                    percent
                )
            )

        print(
            "{}{}Requests have been processed.{}".format(
                TextFormat.OKGREEN,
                TextFormat.BOLD,
                TextFormat.END
            )
        )

    except psycopg2.DatabaseError as error:
        print(
            ''.join(
                [TextFormat.FAIL, TextFormat.BOLD, str(error), TextFormat.END]
            )
        )

    finally:
        return


if __name__ == '__main__':
    most_popular_three_articles()
    most_popular_article_author()
    days_error()
