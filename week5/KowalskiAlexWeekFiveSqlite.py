import sqlite3 as sq;

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
        cursor.execute("CREATE TABLE Music_Artists (artist text, genre text, record_count integer)")

        # Not exactly needed here, but I'm using parametized queuries as a habit for safety (helps prevent sql injection attacks)
        cursor.execute("INSERT INTO Music_Artists values (?,?,?)", ("Miley", "Rock", 14));
        cursor.execute("INSERT INTO Music_Artists values (?,?,?)", ("Dolly", "Country", 123));
        cursor.execute("INSERT INTO Music_Artists values (?,?,?)", ("Brittany", "Rock", 37));

        # Committing in chunks rather than on every execution increases performance, but loses more in the case of a rollback.
        conn.commit();

        # Selections don't need committing since no changes are made to to database or its data
        cursor.execute("SELECT * FROM Music_Artists");
        print("All rows:")

        # selected rows get stored in the cursor where they can be returned using one of the `fetch` functions
        for row in cursor.fetchall():
            print(row);
        cursor.execute("SELECT * FROM Music_Artists WHERE genre='Rock'");
        print("\nAll rows with genre = 'Rock':")
        for row in cursor.fetchall():
            print(row);
        conn.commit();
    except sq.Error as err:
        print(f"Failed to open database `mydatabase.db`: {err}")
    finally:
        if conn != None:
            conn.close();

if __name__ == "__main__":
    main();
