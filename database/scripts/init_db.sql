CREATE TABLE IF NOT EXISTS 
    age_group (
        age_group_id SMALLINT,
        group_name VARCHAR(10) UNIQUE NOT NULL,
        PRIMARY KEY(age_group_id) 
    );

CREATE TABLE IF NOT EXISTS 
    client (
        client_id BIGINT,
        age_group_id SMALLINT,
        client_sex BOOLEAN,
        FOREIGN KEY (age_group_id)
            REFERENCES age_group(age_group_id),
        PRIMARY KEY(client_id)
    );

CREATE TABLE IF NOT EXISTS
    author (
        author_id BIGINT,
        author_name VARCHAR (200) NOT NULL,
        PRIMARY KEY(author_id)
    );

CREATE TABLE IF NOT EXISTS
    genre (
        genre_id SMALLINT,
        genre_name VARCHAR(200) UNIQUE NOT NULL,
        PRIMARY KEY(genre_id) 
    );

CREATE TABLE IF NOT EXISTS
    book (
        book_id BIGINT, 
        book_title VARCHAR(300) NOT NULL,
        book_issue_year SMALLINT,
        PRIMARY KEY(book_id)
    );

CREATE TABLE IF NOT EXISTS
    book_genre (
        book_id BIGINT,
        genre_id SMALLINT,
        FOREIGN KEY (book_id)
            REFERENCES book(book_id),
        FOREIGN KEY (genre_id)
            REFERENCES genre(genre_id),
        PRIMARY KEY (book_id, genre_id)
    );

CREATE TABLE IF NOT EXISTS
    book_author (
        book_id BIGINT,
        author_id SMALLINT,
        PRIMARY KEY (book_id, author_id),
        FOREIGN KEY (book_id)
            REFERENCES book(book_id),
        FOREIGN KEY (author_id)
            REFERENCES author(author_id)
    );

CREATE TABLE IF NOT EXISTS
    ratings (
        client_id BIGINT,
        book_id BIGINT, 
        progress SMALLINT,
        rating SMALLINT,
        start_date TIMESTAMP,
        FOREIGN KEY (client_id)
            REFERENCES client(client_id),
      	FOREIGN KEY (book_id)
            REFERENCES book(book_id),
        PRIMARY KEY (client_id, book_id, start_date)
    );