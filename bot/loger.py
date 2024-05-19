import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename='bot.log'
)

logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

def error_handler(update, context):
    user = update.message.from_user
    logger.error(f"ERROR in {user.username} ({user.id}): {context.error}")