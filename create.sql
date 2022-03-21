-- @BLOCK
CREATE TABLE Images (
    id INT PRIMARY KEY AUTO_INCREMENT,
    description TEXT,
    height INT,
    width INT,
    url VARCHAR(2083)
)
--

-- @BLOCK
CREATE TABLE Authors (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR NOT NULL,
    url VARCHAR(2083)
)
--

-- @BLOCK
CREATE TABLE Ingredients (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR NOT NULL UNIQUE
)
--

-- @BLOCK 
CREATE TABLE Instructions (
    id INT PRIMARY KEY AUTO_INCREMENT,
    instruction TEXT NOT NULL
)
--

-- @BLOCK
CREATE TABLE Cuisines (
    id INT PRIMARY KEY AUTO_INCREMENT,
    cuisine VARCHAR NOT NULL UNIQUE
)
--

-- @BLOCK
CREATE TABLE Keywords (
    id INT PRIMARY KEY AUTO_INCREMENT,
    keyword VARCHAR NOT NULL UNIQUE
)
--

-- @BLOCK
CREATE TABLE Categories (
    id INT PRIMARY KEY,
    category VARCHAR NOT NULL UNIQUE
)
--

-- @BLOCK
CREATE TABLE Recipies(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR NOT NULL,
    imageId INT REFERENCES Images(id),
    authorId INT REFERENCES Authors(id),
    datePublished DATETIME,
    description TEXT,
    prepTime VARCHAR,
    cookTime VARCHAR,
    totalTime VARCHAR,
    servings INT,
    ratingCount INT,
    ratingValue FLOAT,
    url VARCHAR(2083) NOT NULL UNIQUE,
    urlHash VARCHAR NOT NULL
)

CREATE INDEX IX_Recipies_urlHash
ON Recipies(urlHash)
--

-- @BLOCK
CREATE TABLE RecipeInstructions(
    recipeId INT NOT NULL REFERENCES Recipies(id),
    ingredientId INT NOT NULL REFERENCES Ingredients(id),
    ingredientQty INT,
    ingredientUnit VARCHAR
)
--

--@BLOCK
CREATE TABLE RecipeInstructions (
    reciepId INT NOT NULL REFERENCES Recipies(id),
    instructionId INT NOT NULL REFERENCES Instructions(id),
    step INT NOT NULL
)
CREATE INDEX IX_RecipeInstructions_Recipe
ON RecipeInstructions(recipeId)

CREATE INDEX IX_RecipeInstructions_Instruction
on RecipeInstructions(instructionId)
--

--@BLOCK
CREATE TABLE RecipeCuisines(
    recipeId INT NOT NULL REFERENCES Recipe(id),
    cuisineId INT NOT NULL REFERENCES Cuisines(id)
)

CREATE INDEX IX_RecipeCuisines_Recipe
ON RecipeCuisines(recipeId)

CREATE INDEX IX_RecipeCuisines_Cuisine
ON RecipeCuisines(cuisineId)
--

--@BLOCK
CREATE TABLE RecipeKeywords(
    recipeId INT NOT NULL REFERENCES Recipies(id),
    keywordId INT NOT NULL REFERENCES Keywords(id)
)

CREATE INDEX IX_RecipeKeywords_Recipe
ON RecipeKeywords(recipeId)

CREATE INDEX IX_RecipeKeywords_Keyword
ON RecipeKeywords(keywordId)
--

--@BLOCK
CREATE TABLE RecipeCategories(
    recipeId INT NOT NULL REFERENCES Recipies(id),
    categoryId INT NOT NULL REFERENCES Categories(id)
)

CREATE INDEX IX_RecipeCategories_Recipe
ON RecipeCategories(recipeId)

CREATE INDEX IX_RecipeCategories_Category
ON RecipeCategories(categoryId)
--