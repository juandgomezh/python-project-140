# Constantes por juego en un diccionario para facilitar el entendimiento y
# la mantenibilidad del proyecto...
GAMES_CONSTANTS = {
    "ALL": {
        "MIN_NUMBER": 1,
    },
    "CALC": {
        "DESCRIPTION": "What is the result of the expression?",
        "MAX_NUMBER": 50,
        "OPERATIONS": ["+", "-", "*"],
    },
    "PROGRESSION": {
        "DESCRIPTION": "What number is missing in the progression?",
        "PROGRESSION_SIZE": 10,
        "MAX_NUMBER": 20,
        "MIN_STEP_NUMBER": 0,
        "MAX_STEP_NUMBER": 9,
    },
    "EVEN": {
        "MAX_NUMBER": 100,
        "DESCRIPTION": (
            'Answer "yes" if the number is even, otherwise answer "no".'
        ),
    },
    "GCD": {
        "MAX_NUMBER": 100,
        "DESCRIPTION": "Find the greatest common divisor of given numbers.",
    },
    "PRIME": {
        "MAX_NUMBER": 100,
        "DESCRIPTION": (
            'Answer "yes" if given number is prime. Otherwise answer "no".',
        ),
    },
}
