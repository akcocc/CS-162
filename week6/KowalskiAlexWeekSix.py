import sqlite3 as sq;

def print_rows(cursor: sq.Cursor):
    # selected rows get stored in the cursor where they can be returned using one of the `fetch` functions
    # or simply capturing each with a `for` loop as it's done here
    for row in cursor:
        for i in range(len(row)):
            column = row[i];
            print(f"{column}", end="");
            if i != len(row) - 1:
                print(", ", end="");
        print();

def main():
    """
    Main Entry Point
    """
    conn = None;
    try:
        conn =  sq.connect("mydatabase.db");
        cursor = conn.cursor();
        # Dropping the table for a clean slate so no duplicate data is inserted
        cursor.execute("DROP TABLE IF EXISTS Music_Artists");
        cursor.execute("DROP TABLE IF EXISTS Genres");
        cursor.execute("DROP TABLE IF EXISTS Cities");
        cursor.execute("CREATE TABLE Music_Artists (artist text, genre text, record_count integer)")
        cursor.execute("CREATE TABLE Genres (genre text, city text)")
        cursor.execute("CREATE TABLE Cities (city text, state text, zip_code integer, population integer)")

        # Not exactly needed here, but I'm using parametized queuries as a habit for safety (helps prevent sql injection attacks)
        cursor.execute("INSERT INTO Music_Artists values (?,?,?)", ("Miley", "Rock", 14));
        cursor.execute("INSERT INTO Music_Artists values (?,?,?)", ("Dolly", "Country", 123));
        cursor.execute("INSERT INTO Music_Artists values (?,?,?)", ("Brittany", "Rock", 37));

        # Committing in chunks rather than on every execution increases performance, but loses more in the case of a rollback.
        conn.commit();

        cursor.execute("INSERT INTO Genres values (?,?)", ("Rock", "Los Angeles"));
        cursor.execute("INSERT INTO Genres values (?,?)", ("Hippie", "Eugene"));
        cursor.execute("INSERT INTO Genres values (?,?)", ("Opera", "Florence"));

        conn.commit();

        cursor.execute("INSERT INTO Cities values (?,?,?,?)", ("Los Angeles", "CA", 66666, 10_000_000));
        cursor.execute("INSERT INTO Cities values (?,?,?,?)", ("Eugene", "OR", 55555, 80_000));
        cursor.execute("INSERT INTO Cities values (?,?,?,?)", ("Nashville", "TN", 11111, 1_500_000));

        conn.commit();

        # Selections don't need committing since no changes are made to to database or its data
        cursor.execute("SELECT * FROM Music_Artists");
        print("All rows:")

        print_rows(cursor);
        cursor.execute("SELECT * FROM Music_Artists WHERE genre='Rock'");
        print("\nAll rows with genre = 'Rock':")
        print_rows(cursor);

        # Don't need to specify the join as an inner join as that's already the
        # default joining behavior
        cursor.execute("SELECT artist FROM Music_Artists JOIN Genres USING ( genre )");

        print("\nJoined Artists using 'Genres' Table:")
        print_rows(cursor);

        cursor.execute("SELECT artist FROM Music_Artists");
        print("\nWhich artist would you like to know more about?")
        print()
        print_rows(cursor);

        chosen_artist = input("Artist: ").casefold();

        cursor.execute("SELECT * FROM Music_Artists where (artist=?)", (chosen_artist.capitalize(),));

        if cursor.rowcount == 0:
            print(f"Couldn't find any information for the artist: {chosen_artist.capitalize()}");
            exit(0)

        artist_row = cursor.fetchone();

        artist = artist_row[0];
        genre = artist_row[1];
        record_count = artist_row[2];

        cursor.execute("SELECT city, population FROM Genres JOIN Cities USING ( city ) where genre = ?", (genre,));

        print(f"{genre} artist, {artist}, has {record_count} recordings and is ", end="");
        print(cursor.rowcount);
        if cursor.rowcount == 0:
            print("popular everywhere");
        else:
            genre_row = cursor.fetchone();
            city = genre_row[0];
            population = genre_row[1];
            print(f"most popular in {city} with a population of {population}");

    except sq.Error as err:
        print(f"Failed to open database `mydatabase.db`: {err}")
    finally:
        if conn != None:
            conn.close();

if __name__ == "__main__":
    main();
