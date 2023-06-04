CREATE TABLE IF NOT EXISTS 
    clients (
        client_id BIGINT,
        client_age SMALLINT,
        client_sex BOOLEAN,
        PRIMARY KEY(client_id)
    );

CREATE TABLE IF NOT EXISTS
    authors (
        author_id BIGINT,
        author_name VARCHAR (200) NOT NULL,
        PRIMARY KEY(author_id)
    );

CREATE TABLE IF NOT EXISTS
    genres (
        genre_id SMALLINT,
        genre_name VARCHAR(200) UNIQUE NOT NULL,
        PRIMARY KEY(genre_id) 
    );

CREATE TABLE IF NOT EXISTS
    books (
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
            REFERENCES books(book_id),
        FOREIGN KEY (genre_id)
            REFERENCES genres(genre_id),
        PRIMARY KEY (book_id, genre_id)
    );

CREATE TABLE IF NOT EXISTS
    book_author (
        book_id BIGINT,
        author_id SMALLINT,
        PRIMARY KEY (book_id, author_id),
        FOREIGN KEY (book_id)
            REFERENCES books(book_id),
        FOREIGN KEY (author_id)
            REFERENCES authors(author_id)
    );

CREATE TABLE IF NOT EXISTS
    ratings (
        client_id BIGINT,
        book_id BIGINT, 
        progress SMALLINT,
        rating SMALLINT,
        start_date BIGINT,
        FOREIGN KEY (client_id)
            REFERENCES clients(client_id),
      	FOREIGN KEY (book_id)
            REFERENCES books(book_id),
        PRIMARY KEY (client_id, book_id, start_date)
    );