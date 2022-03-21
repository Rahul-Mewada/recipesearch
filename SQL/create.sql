-- IMAGES TABLE
-- @BLOCK
CREATE TABLE Images (
    id INT PRIMARY KEY AUTO_INCREMENT,
    description TEXT,
    height INT,
    width INT,
    url VARCHAR(2083)
)
--


-- AUTHORS TABLE
-- @BLOCK
CREATE TABLE Authors (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(64) NOT NULL,
    url VARCHAR(2083)
)
--


-- INGREDIENTS TABLE
-- @BLOCK
CREATE TABLE Ingredients (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(64) NOT NULL UNIQUE
)
--


-- INSTRUCTIONS TABLE
-- @BLOCK 
CREATE TABLE Instructions (
    id INT PRIMARY KEY AUTO_INCREMENT,
    instruction TEXT NOT NULL
)
--


-- CUISINES TABLE
-- @BLOCK
CREATE TABLE Cuisines (
    id INT PRIMARY KEY AUTO_INCREMENT,
    cuisine VARCHAR(64) NOT NULL UNIQUE
)
--


-- KEYWORDS TABLE
-- @BLOCK
CREATE TABLE Keywords (
    id INT PRIMARY KEY AUTO_INCREMENT,
    keyword VARCHAR(64) NOT NULL UNIQUE
)
--


-- CATEGORIES TABLE
-- @BLOCK
CREATE TABLE Categories (
    id INT PRIMARY KEY,
    category VARCHAR(64) NOT NULL UNIQUE
)
--


-- RECIPE TABLE
-- @BLOCK
CREATE TABLE Recipies(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(128) NOT NULL,
    imageId INT REFERENCES Images(id),
    authorId INT REFERENCES Authors(id),
    datePublished DATETIME,
    description TEXT,
    prepTime VARCHAR(32),
    cookTime VARCHAR(32),
    totalTime VARCHAR(32),
    servings VARCHAR(32),
    ratingCount INT,
    ratingValue FLOAT,
    url VARCHAR(255) NOT NULL UNIQUE,
    urlHash BIGINT NOT NULL
)
--
-- @BLOCK
CREATE INDEX IX_Recipies_urlHash 
ON Recipies(urlHash)
--


-- RECIPE INSTRUCTIONS JUNCTION TABLE
--@BLOCK
CREATE TABLE RecipeInstructions (
    recipeId INT NOT NULL REFERENCES Recipies(id),
    instructionId INT NOT NULL REFERENCES Instructions(id),
    step INT NOT NULL
)
--
-- @BLOCK
CREATE INDEX IX_RecipeInstructions_Recipe 
ON RecipeInstructions(recipeId)
--
-- @BLOCK
CREATE INDEX IX_RecipeInstructions_Instruction 
ON RecipeInstructions(instructionId)
--


-- RECIPE INGREDIENTS JUNCTION TABLE
-- @BLOCK
CREATE TABLE RecipeIngredients (
    recipeId INT NOT NULL REFERENCES Recipies(id),
    ingredientId INT NOT NULL REFERENCES Ingredients(id),
    ingredientQty FLOAT,
    ingredientUnit VARCHAR(32)
)
--
-- @BLOCK
CREATE INDEX IX_RecipeIngredients_Recipe
ON RecipeIngredients(recipeId)
-- @BLOCK
CREATE INDEX IX_RecipeIngredients_Ingredient
ON RecipeIngredients(ingredientId)
--


-- RECIPE CUISINES JUNCTION TABLE
--@BLOCK
CREATE TABLE RecipeCuisines(
    recipeId INT NOT NULL REFERENCES Recipe(id),
    cuisineId INT NOT NULL REFERENCES Cuisines(id)
)
--
--@BLOCK
CREATE INDEX IX_RecipeCuisines_Recipe
ON RecipeCuisines(recipeId)
--
--@BLOCK
CREATE INDEX IX_RecipeCuisines_Cuisine
ON RecipeCuisines(cuisineId)
--


-- RECIPE KEYWORDS JUNCTION TABLE
--@BLOCK
CREATE TABLE RecipeKeywords(
    recipeId INT NOT NULL REFERENCES Recipies(id),
    keywordId INT NOT NULL REFERENCES Keywords(id)
)
--
--@BLOCK
CREATE INDEX IX_RecipeKeywords_Recipe
ON RecipeKeywords(recipeId)
--
--@BLOCK
CREATE INDEX IX_RecipeKeywords_Keyword
ON RecipeKeywords(keywordId)
--


-- RECIPE CATEGORIES JUNCTION TABLE
--@BLOCK
CREATE TABLE RecipeCategories(
    recipeId INT NOT NULL REFERENCES Recipies(id),
    categoryId INT NOT NULL REFERENCES Categories(id)
)
--
--@BLOCK
CREATE INDEX IX_RecipeCategories_Recipe
ON RecipeCategories(recipeId)
--
--@BLOCK
CREATE INDEX IX_RecipeCategories_Category
ON RecipeCategories(categoryId)
--