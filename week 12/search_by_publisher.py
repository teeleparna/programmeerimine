
import sqlite3


def get_games_by_publisher(publisher_name):
    conn = sqlite3.connect("TopGamesDB.db")
    cursor = conn.cursor()

    query = """
    SELECT Game.name, Publisher.name
    FROM Game
    JOIN GamePublisher ON Game.id = GamePublisher.gameId
    JOIN Publisher ON Publisher.id = GamePublisher.publisherId
    WHERE LOWER(Publisher.name) = LOWER(?)
    ORDER BY Game.name;
    """

    cursor.execute(query, (publisher_name,))
    results = cursor.fetchall()

    for game in results:
        print(game)

    conn.close()


get_games_by_publisher("Nintendo")
