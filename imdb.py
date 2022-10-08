import requests
from bs4 import BeautifulSoup
from config import host, user, password, db_name
import psycopg2


def films(genr):
    for i in range(1, 9051, 50):
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0'
        }

        url = f'https://www.imdb.com/search/title/?title_type=movie&genres={genr}&sort=num_votes,desc&start={i}&explore=title_type,genres'
        print(f'{i}:')

        q = requests.get(url=url, headers=headers, timeout=5)
        result = q.text

        soup = BeautifulSoup(result, 'lxml')

        page = soup.find_all(class_='lister-item-content')
        stars = []
        headers = []
        votes = []
        links = []

        for link in page: # Цикл достающий ссылки из тэгов названий фильмов
            link = link.find_all('h3', class_='lister-item-header')
            for a in link:
                a = a.find_all("a")
                for link in a:
                    link = link.get('href')
                    links.append(link)

        for header in page: # Цикл достающий заголовки 
            header = header.find_all('h3', class_= 'lister-item-header')
            for a in header:
                a = a.find('a')
                for header in a:
                    header = header.get_text()
                    header = header.strip()
                    header = header.replace("'", "''")
                    headers.append(header)

        for star in page: # Цикл достающий показатели звёздочек
            star = star.find_all('div', class_='ratings-bar')
            for strong in star:
                strong = strong.find_all('strong')
                for star in strong:
                    star = star.get_text()
                    stars.append(star)

        for vote in page: # Цикл достающий кол-во просмотров
            vote = vote.find_all('p', class_='sort-num_votes-visible')
            for span in vote:
                span = span.find_all("span")
                for vote in span:
                    if vote.attrs.get("name"):
                        vote = vote.get_text()
                        vote = vote.replace(',', '')
                        if vote[0] == '$':
                            continue
                        if int(vote) < 100000:
                            break
                        votes.append(vote)
        
        for vote in votes: # Убираем из списка просмотров показатели сборов (Они находятся в одном тэге, поэтому достаются с просмотрами)
            if vote[0] == '$':
                votes.remove(vote)

        hsvlist = []

        try: # try ля предотвращения ошибки из-за несоответствия кол-ва просмотров с заголовками
            for i in range(len(headers)): # цикл отбирающий фильмы по заданным показателям. 
                hsv = headers[i], stars[i], votes[i], links[i]
                if float(hsv[1]) <= 7.5:
                    del hsv
                elif int(hsv[2]) > 700000:
                    del hsv
                else:
                    hsvlist.append(hsv)
        except Exception as _ex:
            break
        
        if len(hsvlist) >= 1: # Заносит в БД список, если он не пуст
            try:
                con = psycopg2.connect(
                    host = host,
                    user = user,
                    password = password,
                    database = db_name
                )
                con.autocommit = True

                for hsv in hsvlist:
                    with con.cursor() as cursor:
                        cursor.execute(
                            """INSERT INTO {} (header, stars, votes, link) VALUES 
                            ('{}','{}','{}','{}')""".format(genr, hsv[0], hsv[1], hsv[2], hsv[3])
                        )
                        cursor.execute(
                            """DELETE FROM {} WHERE ctid NOT IN
                                (SELECT max(ctid) FROM {} GROUP BY header);""".format(genr, genr)
                        )

            except Exception as _ex:
                print('[INFO] Error while working with PostgreSQL', _ex)
            finally:
                if con:
                    con.close()
                    print('[INFO] PostgreSQL connection closed')
        else:
            print('The list is empty')

def database(): # Обновляет БД 
    try:
        con = psycopg2.connect(
            host = host,
            user = user,
            password = password,
            database = db_name
        )
        con.autocommit = True

        with con.cursor() as cursor:
            cursor.execute(
                """DROP TABLE drama, comedy, musical, romance, horror, fantasy, action""")

    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)
    finally:
        if con:
            con.close()
            print('[INFO] PostgreSQL connection closed')

    try:
        con = psycopg2.connect(
            host = host,
            user = user,
            password = password,
            database = db_name
        )
        con.autocommit = True

        with con.cursor() as cursor:
            cursor.execute(
                """CREATE TABLE drama(
                    header text NOT NULL,
                    stars float NOT NULL,
                    votes int NOT NULL,
                    link text NOT NULL);

                    CREATE TABLE comedy(
                    header text NOT NULL,
                    stars float NOT NULL,
                    votes int NOT NULL,
                    link text NOT NULL);

                    CREATE TABLE musical(
                    header text NOT NULL,
                    stars float NOT NULL,
                    votes int NOT NULL,
                    link text NOT NULL);

                    CREATE TABLE romance(
                    header text NOT NULL,
                    stars float NOT NULL,
                    votes int NOT NULL,
                    link text NOT NULL);

                    CREATE TABLE horror(
                    header text NOT NULL,
                    stars float NOT NULL,
                    votes int NOT NULL,
                    link text NOT NULL);
                    
                    CREATE TABLE fantasy(
                    header text NOT NULL,
                    stars float NOT NULL,
                    votes int NOT NULL,
                    link text NOT NULL);
                    
                    CREATE TABLE action(
                    header text NOT NULL,
                    stars float NOT NULL,
                    votes int NOT NULL,
                    link text NOT NULL);"""
            )

            print('[INFO] Table created succesfully')

    except Exception as _ex:
        print('[INFO] Error while working with PostgreSQL', _ex)
    finally:
        if con:
            con.close()
            print('[INFO] PostgreSQL connection closed')

        
def main():
    database()
    films()


if __name__ == '__main__':
    main()

