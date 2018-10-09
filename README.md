# Log analysis

 ## Description:
This is an internal reporting tool that it uses information from the database
to discover what kind of articles the site's readers like.
The database contains newspaper articles, as well as the web server
 log for the site. The log has a database row for each time a reader
loaded a web page. Using that information, this code answers
questions about the site's user activity.
 The program runs from the command line. It does not take any input from the user.
Instead, it connects to that database, uses SQL queries to analyze the log data,
 and prints out the answers to some questions:
1. *What are the most popular three articles of all time?*
2. *Who are the most popular article authors of all time?*
3. *On which days did more than 1% of requests lead to errors?*

  ## Installation:
This project runs on pyhon3 and postgresql on ubuntu viraual env.(I highly 
recomend to use vagrant and to run vagrant up using Vagrantfile from the project. 
It will install all dependencies and will create 'news' database for you. 
If you have vagrant up and running you can ignore steps 4 and 5. To have success installing
VM on your coumputer visit: 1. *www.virtualbox.org* 2. *www.vagrantup.com*.)

1. **apt-get update**
2. **apt-get install git-core**
3. **git clone https://github.com/airdenis/log_analysis.git**
4. **pip install -r requirements.txt**
5. create a database named news.
6. download data from "https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip"
7. **psql -d news -f newsdata.sql**
8. run **python3 db_view.py** to create database views (
         * The first view is named v_articles_authors_log. It aggregates all three
               tables and returns article title column and authors column. 
         * The second view is named v_errors. It retuns requests group by dates excluding  HTTP status code '200 OK').
         * The third view is name v_total. It returns total requests group by dates.
 9. run **python3 log_analysis.py** to get the results.
