import random
import logging

# Configure logging
logging.basicConfig(
    format='%(asctime)s [%(levelname)s] - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO
)

logger = logging.getLogger()


def generate_random_answer(event, context):
    try:
        # List of possible answers
        answers = ["yes", "no", "maybe"]

        # Generate a random answer
        random_answer = random.choice(answers)

        logger.info(f"Generated random answer: {random_answer}")

        return {
            "statusCode": 200,
            "body": random_answer,
            "headers": {
                "Content-Type": "application/json"
            }
        }

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        return {
            "statusCode": 500,
            "body": "Internal Server Error",
            "headers": {
                "Content-Type": "application/json"
            }
        }
