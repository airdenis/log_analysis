#!/usr/bin/python3
from text_format import TextFormat as TF
import psycopg2


def create_articles_authors_log_view():
    try:
        db = psycopg2.connect("dbname=news")
        c = db.cursor()
        c.execute('''CREATE VIEW v_articles_authors_log AS
                        SELECT articles.title AS articles,
                                authors.name AS authors
                        FROM articles, authors, log
                        WHERE articles.slug = SUBSTRING(log.path, 10) and
                              articles.author = authors.id;''')
        db.commit()
        db.close()

        print(
            "{}{}'v_articles_authors_log' created.{}".format(
                TF.OKGREEN,
                TF.BOLD,
                TF.END
            )
        )

    except psycopg2.DatabaseError as error:
        print(
            ''.join(
                [TF.FAIL, TF.BOLD, str(error), TF.END]
            )
        )

    finally:
        return


def create_errors_view():
    try:
        db = psycopg2.connect("dbname=news")
        c = db.cursor()
        c.execute('''CREATE VIEW v_errors AS
                        SELECT time::timestamp::date AS date,
                        COUNT(*) AS errors_count
                        FROM log
                        WHERE status != '200 OK'
                        GROUP BY time::timestamp::date;''')
        db.commit()
        db.close()

        print(
            "{}{}'v_errors' created.{}".format(
                TF.OKGREEN,
                TF.BOLD,
                TF.END
            )
        )

    except psycopg2.DatabaseError as error:
        print(
            ''.join(
                [TF.FAIL, TF.BOLD, str(error), TF.END]
            )
        )

    finally:
        return


def create_total_view():
    try:
        db = psycopg2.connect("dbname=news")
        c = db.cursor()
        c.execute('''CREATE VIEW v_total AS
                        SELECT time::timestamp::date AS date,
                            COUNT(*) AS total_count
                        FROM log
                        GROUP BY time::timestamp::date;''')
        db.commit()
        db.close()

        print(
            "{}{}'v_total' created.{}".format(
                TF.OKGREEN,
                TF.BOLD,
                TF.END
            )
        )

    except psycopg2.DatabaseError as error:
        print(
            ''.join(
                [TF.FAIL, TF.BOLD, str(error), TF.END]
            )
        )

    finally:
        return


if __name__ == "__main__":
    create_articles_authors_log_view()
    create_errors_view()
    create_total_view()
