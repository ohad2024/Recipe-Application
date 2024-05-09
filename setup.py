import sqlite3

def create_db():
    connection = sqlite3.connect('recipes.db')
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recipes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            ingredients TEXT NOT NULL,
            instructions TEXT NOT NULL
        )
    ''')
    # Insert recipes with detailed instructions and run this one time befor you run app.py
    cursor.executemany('''
        INSERT INTO recipes (title, ingredients, instructions)
        VALUES (?, ?, ?)
    ''', [
        ('Shakshuka', 'Eggs, Tomato sauce, Onion, Bell pepper, Garlic, Spices',
         'Saute onions and garlic in olive oil until golden. Add chopped bell peppers, cook until soft. Pour in tomato sauce, add spices like cumin, paprika, and cayenne, and simmer for 10 minutes. Crack eggs into the pan. Cover and cook until eggs are just set.'),
        ('Falafel', 'Chickpeas, Herbs, Spices, Garlic, Onion',
         'Soak chickpeas overnight, then blend with herbs like parsley and cilantro, garlic, onion, and spices. Form into balls or patties and deep fry until golden and crispy.'),
        ('Hummus', 'Cooked chickpeas, Tahini, Lemon juice, Garlic, Olive oil',
         'Blend cooked chickpeas with tahini, lemon juice, and garlic in a food processor. Slowly add olive oil until smooth. Season with salt and serve with a drizzle of olive oil and paprika.'),
        ('Sabich', 'Eggplant, Hard-boiled eggs, Tahini, Amba, Pita',
         'Fry slices of eggplant until golden. Assemble the pita with fried eggplant, sliced hard-boiled eggs, tahini, and amba.'),
        ('Israeli Salad', 'Cucumber, Tomato, Onion, Bell pepper, Lemon juice, Olive oil',
         'Dice cucumber, tomato, onion, and bell pepper. Toss with lemon juice, olive oil, salt, and pepper.'),
        ('Shawarma', 'Chicken or beef, Shawarma spices, Onion, Tomato, Cucumber, Tahini sauce, Pita',
         'Marinate meat in shawarma spices and olive oil. Grill until cooked. Serve sliced in pita with vegetables and tahini sauce.'),
        ('Jerusalem Kugel', 'Noodles, Sugar, Eggs, Black pepper, Oil',
         'Caramelize sugar into a deep golden color, careful not to burn. Mix cooked noodles with caramelized sugar, beaten eggs, and season with black pepper. Bake until set.'),
        ('Challah', 'Flour, Yeast, Eggs, Sugar, Salt, Sesame seeds',
         'Mix flour with sugar, yeast, and salt. Add eggs and oil, knead until smooth. Let rise until doubled. Braid the dough, let rise again, then brush with beaten egg, sprinkle with sesame seeds, and bake.'),
        ('Stuffed Cabbage', 'Cabbage, Ground beef, Rice, Onion, Tomato sauce',
         'Blanch cabbage leaves until pliable. Mix ground beef with cooked rice and chopped onion, season. Wrap meat mixture in cabbage leaves, cover with tomato sauce, and simmer until cooked.'),
        ('Kubbeh', 'Bulghur wheat, Ground beef, Onions, Pine nuts, Spices',
         'Mix soaked bulghur with ground beef, form into a shell. Fill with cooked beef and onions, seasoned with allspice and cinnamon. Fry or bake until crisp.'),
        ('Knafeh', 'Kadaif noodles, Cheese, Sugar syrup, Rose water',
         'Layer kadaif noodles with cheese, bake until golden. Pour over cooled sugar syrup flavored with rose water.'),
        ('Rugelach', 'Dough, Chocolate or jam, Nuts, Sugar',
         'Roll dough around filling of choice, typically chocolate or jam and nuts. Bake until golden and sprinkle with sugar.'),
        ('Malabi', 'Milk, Sugar, Cornstarch, Rose water, Pistachios, Coconut',
         'Cook milk with sugar and cornstarch until thick. Flavor with rose water. Chill, then garnish with chopped pistachios and coconut.')
    ])
    connection.commit()
    connection.close()



if __name__ == '__main__':
    create_db()
