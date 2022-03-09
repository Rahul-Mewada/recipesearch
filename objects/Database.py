from config import Config
import mysql.connector

"""
("CREATE TABLE TestRecipe ( \
    name VARCHAR(140), imageDescription text, imageHeight int, imageWidth int, imageUrl VARCHAR(2083), \
        authorName VARCHAR(140), authorUrl VARCHAR(2083), datePublished VARCHAR(100), description text, \
            prepTime VARCHAR(100), cookTime VARCHAR(100), totalTime VARCHAR(100), keywords text, \
                servings VARCHAR(100), category text, cuisine text, ingredients text, instructions text, \
                    ratingsCount int, recipeValue float)")
"""

class Database:
    def __init__(self):
        self.db = mysql.connector.connect(
            host = Config.DATABASE_CONFIG['server'],
            user = Config.DATABASE_CONFIG['user'],
            passwd = Config.DATABASE_CONFIG['password'],
            database = Config.DATABASE_CONFIG['name']
        )
        self.cursor = self.db.cursor()

    def insert_recipe(self, recipe):
        sql_query = "INSERT INTO TestRecipe (name, imageDescription, imageHeight, imageWidth, imageUrl, \
            authorName, authorUrl, datePublished, description, prepTime, cookTime, totalTime, keywords, \
                servings, category, cuisine, ingredients, instructions, ratingsCount, recipeValue) \
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(sql_query, recipe.to_sql())
        self.db.commit()

    def print_entries(self):
        print("Printing Entries")
        self.cursor.execute("SELECT * FROM TestRecipe")
        for x in self.cursor:
            print(x)