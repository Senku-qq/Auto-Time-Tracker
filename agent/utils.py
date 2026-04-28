import logging
logging.basicConfig(
    filename=r"C:\Users\manyt\Desktop\Time-tracker\Auto-Time-Tracker\logs\logs.log",
    encoding="UTF-8",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    )
logger = logging.getLogger(__name__)  