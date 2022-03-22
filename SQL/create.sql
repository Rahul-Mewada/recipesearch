CREATE TABLE Images (
    id INT PRIMARY KEY AUTO_INCREMENT,
    description TEXT,
    height INT,
    width INT,
    url VARCHAR(2083)
);



CREATE TABLE Authors (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(64) NOT NULL,
    url VARCHAR(2083)
);



CREATE TABLE Ingredients (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(64) NOT NULL UNIQUE
);



CREATE TABLE Instructions (
    id INT PRIMARY KEY AUTO_INCREMENT,
    instruction TEXT NOT NULL
);




CREATE TABLE Cuisines (
    id INT PRIMARY KEY AUTO_INCREMENT,
    cuisine VARCHAR(64) NOT NULL UNIQUE
);



CREATE TABLE Keywords (
    id INT PRIMARY KEY AUTO_INCREMENT,
    keyword VARCHAR(64) NOT NULL UNIQUE
);



CREATE TABLE Categories (
    id INT PRIMARY KEY,
    category VARCHAR(64) NOT NULL UNIQUE
);



CREATE TABLE Recipies(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(128) NOT NULL,
    imageId INT,
    authorId INT,
    datePublished DATETIME,
    description TEXT,
    prepTime VARCHAR(32),
    cookTime VARCHAR(32),
    totalTime VARCHAR(32),
    servings VARCHAR(32),
    ratingCount INT,
    ratingValue FLOAT,
    url VARCHAR(255) NOT NULL UNIQUE,
    urlHash BIGINT NOT NULL,
    FOREIGN KEY (imageId) REFERENCES Images(id),
    FOREIGN KEY (authorId) REFERENCES Authors(id)
);
CREATE INDEX IX_Recipies_urlHash ON Recipies(urlHash);


CREATE TABLE RecipeInstructions (
    recipeId INT NOT NULL,
    instructionId INT NOT NULL,
    step INT NOT NULL,
    FOREIGN KEY (recipeId) REFERENCES Recipies(id),
    FOREIGN KEY (instructionId) REFERENCES Instructions(id),
    UNIQUE `comp_const_RecipeInstructions` (recipeId, instructionId)
);
CREATE INDEX IX_RecipeInstructions_Recipe 
ON RecipeInstructions(recipeId);
CREATE INDEX IX_RecipeInstructions_Instruction 
ON RecipeInstructions(instructionId);



CREATE TABLE RecipeIngredients (
    recipeId INT NOT NULL,
    ingredientId INT NOT NULL,
    ingredientQty FLOAT,
    ingredientUnit VARCHAR(32),
    FOREIGN KEY (recipeId) REFERENCES Recipies(id),
    FOREIGN KEY (ingredientId) REFERENCES Ingredients(id),
    UNIQUE `comp_const_RecipeIngredients` (recipeId, ingredientId)
);
CREATE INDEX IX_RecipeIngredients_Recipe
ON RecipeIngredients(recipeId);
CREATE INDEX IX_RecipeIngredients_Ingredient
ON RecipeIngredients(ingredientId);



CREATE TABLE RecipeCuisines(
    recipeId INT NOT NULL,
    cuisineId INT NOT NULL,
    FOREIGN KEY (recipeId) REFERENCES Recipies(id),
    FOREIGN KEY (cuisineId) REFERENCES Cuisines(id),
    UNIQUE `comp_const_RecipeCuisines` (recipeId, cuisineId)
);
CREATE INDEX IX_RecipeCuisines_Recipe
ON RecipeCuisines(recipeId);
CREATE INDEX IX_RecipeCuisines_Cuisine
ON RecipeCuisines(cuisineId);



CREATE TABLE RecipeKeywords(
    recipeId INT NOT NULL,
    keywordId INT NOT NULL,
    FOREIGN KEY (recipeId) REFERENCES Recipies(id),
    FOREIGN KEY (keywordId) REFERENCES Keywords(id),
    UNIQUE `comp_const_RecipeKeywords` (recipeId, keywordId)
);
CREATE INDEX IX_RecipeKeywords_Recipe
ON RecipeKeywords(recipeId);
CREATE INDEX IX_RecipeKeywords_Keyword
ON RecipeKeywords(keywordId);



CREATE TABLE RecipeCategories(
    recipeId INT NOT NULL,
    categoryId INT NOT NULL,
    FOREIGN KEY (recipeId) REFERENCES Recipies(id),
    FOREIGN KEY (categoryId) REFERENCES Categories(id),
    UNIQUE `comp_const_RecipeCategories` (recipeId, categoryId)
);
CREATE INDEX IX_RecipeCategories_Recipe
ON RecipeCategories(recipeId);
CREATE INDEX IX_RecipeCategories_Category
ON RecipeCategories(categoryId);