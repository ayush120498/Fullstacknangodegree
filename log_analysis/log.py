#!/usr/bin/env python

import psycopg2

DBNAME = "news"


def execute(query):
    # connect to the database
    connection = psycopg2.connect(database=DBNAME)
    # perform database operations
    cursor = connection.cursor()
    # execute the entered query
    cursor.execute(query)
    # fetch the result from the entered query
    result = cursor.fetchall()
    # close the connection with database
    connection.close()
    return result

# Question 1. What are the most popular three articles of all time?


def popArticle():
    query1 = """
        select articles.title,
        count(*) as count_article from
        articles join log
        on log.path like
        concat('/article/%',articles.slug)
        group by articles.title
        order by count_article desc
        limit 3;
            """
    data_ = execute(query1)
    j = 1
    print(" MOST POPULAR ARTICLES ")
    for fetch in data_:
        number = str(j)
        title = fetch[0]
        views = str(fetch[1])
        print(number + ' . ' + title + "  =  " + views + " views ")
        i += 1


# Question 2. Who are the most popular article authors of all time?

def popAuthor():
    query2 = """
        select authors.name,
        count(*) as count from
        authors join articles on
        authors.id = articles.author join log
        on log.path
        like concat('/article/%',articles.slug)
        group by authors.name
        order by count desc
        limit 3;
            """
    data_ = execute(query2)
    j = 1
    print("\n POPULAR AUTHORS ")
    for fetch in data_:
        number = str(j)
        title = fetch[0]
        views = str(fetch[1])
        print(number + ' . ' + title + '  =  ' + views + " views ")
        j += 1


# Question 3. On which days did more than 1% of requests lead to errors?

def error():
    query3 = """
        select totl.day,
        ((allErrors.firstError*100)/totl.secondError)as p
          from(
          select date_trunc('day', time) "day",
          count(*) as firstError
          from log where status like '404%'
          group by day) as allErrors
          join(
          select date_trunc('day',time) "day",
          count(*) as secondError
          from log group by day)
          as totl
          on totl.day =  allErrors.day
          where (
          ((allErrors.firstError*100)/totl.secondError)>1)
          order by p desc;
            """
    data_ = execute(query3)
    print('\n The days when more than 1% of requests lead to error:\n')
    for fetch in data_:
        a = fetch[0].strftime("%B %d, %Y")
        errors = str(fetch[1])
        print(a + " had " + errors + " % " + "errors.")


popArticle()
popAuthor()
error()
