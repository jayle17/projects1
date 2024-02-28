# Criteria importance
criteria_importance = {
    'easy_setup': 3,
    'cross_platform_compatibility': 4,
    'cost': 5,
    'single_user_support': 4,
    'ease_of_backup_and_portability': 5,
    'python_compatibility': 5,
}

# Database ratings
database_ratings = {
    'MSSQL': {
        'easy_setup': 2,
        'cross_platform_compatibility': 3,
        'cost': 1,
        'single_user_support': 4,
        'ease_of_backup_and_portability': 2,
        'python_compatibility': 4,
    },
    'Oracle': {
        'easy_setup': 1,
        'cross_platform_compatibility': 3,
        'cost': 1,
        'single_user_support': 4,
        'ease_of_backup_and_portability': 2,
        'python_compatibility': 4,
    },
    'SQLite': {
        'easy_setup': 5,
        'cross_platform_compatibility': 5,
        'cost': 5,
        'single_user_support': 5,
        'ease_of_backup_and_portability': 5,
        'python_compatibility': 5,
    },
    'MySQL/MariaDB': {
        'easy_setup': 4,
        'cross_platform_compatibility': 5,
        'cost': 5,
        'single_user_support': 3,
        'ease_of_backup_and_portability': 3,
        'python_compatibility': 5,
    },
    'PostgreSQL': {
        'easy_setup': 3,
        'cross_platform_compatibility': 5,
        'cost': 5,
        'single_user_support': 3,
        'ease_of_backup_and_portability': 3,
        'python_compatibility': 5,
    },
    'Microsoft Access': {
        'easy_setup': 4,
        'cross_platform_compatibility': 1,
        'cost': 2,
        'single_user_support': 5,
        'ease_of_backup_and_portability': 4,
        'python_compatibility': 3,
    },
    'LibreOffice Base': {
        'easy_setup': 4,
        'cross_platform_compatibility': 5,
        'cost': 5,
        'single_user_support': 4,
        'ease_of_backup_and_portability': 4,
        'python_compatibility': 3,
    },
}

def calculate_scores(importance, ratings):
    """Calculating the score of the ratings"""
    total_scores = {}
    for db, db_ratings in ratings.items():
        score = sum(importance[crit] * db_ratings.get(crit, 0) for crit in importance)
        total_scores[db] = score
    return total_scores

def find_best_database(scores):
    """Finding the best score """
    return max(scores, key=scores.get), scores[max(scores, key=scores.get)]

# Calculate total scores for each database
total_scores = calculate_scores(criteria_importance, database_ratings)

# Find the best database
best_database, best_score = find_best_database(total_scores)

# Print the scores for comparison
for db, score in total_scores.items():
    print(f"{db}: {score}")

# Print the best database and its score
print(f"\nBest Database for the Project: {best_database} with a score of {best_score}")
