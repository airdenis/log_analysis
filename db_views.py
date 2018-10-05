import psycopg2


def create_articles_authors_log_view():
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
    print("View 'v_articles_authors_log' has been created.")
    return


def create_errors_view():
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute('''CREATE VIEW v_errors AS
                    SELECT time::timestamp::date AS date
                    FROM log
                    WHERE status != '200 OK';''')
    db.commit()
    db.close()
    print("View 'v_errors' has been created.")
    return


if __name__ == "__main__":
    create_articles_authors_log_view()
    create_errors_view()

