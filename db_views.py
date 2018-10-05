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
        print('\033[92m\033[1m' + 
                "'v_articles_authors_log' view successfully has been created." +
                '\033[0m')
    except:
        print('\033[91m\033[1m' +
                "Failed to create 'v_articles_authors_log' view." +
                '\033[0m')
    finally:
        return


def create_errors_view():
    try:
        db = psycopg2.connect("dbname=news")
        c = db.cursor()
        c.execute('''CREATE VIEW v_errors AS
                        SELECT time::timestamp::date AS date
                        FROM log
                        WHERE status != '200 OK';''')
        db.commit()
        db.close()
        print('\033[92m\033[1m' +
                "'v_errors' view successfully has been created." +
                '\033[0m')

    except:
        print('\033[91m\033[1m' +
                "Failed to create 'v_errors' view." +
                '\033[0m')
    finally:
        return


if __name__ == "__main__":
    create_articles_authors_log_view()
    create_errors_view()

