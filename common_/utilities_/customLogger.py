from pathlib import Path
import logging
import os
from datetime import datetime


def _get_root_directory():
    """
        Get the root directory of the project based on the current file's location.

        Returns:
            pathlib.Path: Path object representing the root directory of the project.

        Raises:
            FileNotFoundError: If the project directory is not found.
            Exception: For unexpected errors.

        Note:
            -This method extracts the project root path based on the project name "Amazon" and the current file's location.
    """
    try:
        projectName = "Amazon"
        currentPath = Path(__file__)
        projectRootPath = Path((str(currentPath).split(projectName))[0]) / projectName

        return projectRootPath

    except FileNotFoundError as e:
        print(f"Error: The directory was not found: {str(e)}")
        exit(6)
    except Exception as e:
        print(f"Error: An unexpected error occurred: {str(e)}")
        exit(5)


def logger(level, message, fileName=os.path.join(_get_root_directory(), 'logs_', f'log_{datetime.now().strftime("%d_%m_%Y_%H-%M-%S")}.log')):
    """
        Log messages at different log levels (INFO, DEBUG, WARNING, ERROR, CRITICAL) with exception handling.

        This function configures a logger to write log messages to a specified file. It supports multiple log levels:
        - INFO: Informational messages
        - DEBUG: Debugging messages
        - WARNING: Warnings
        - ERROR: Errors
        - CRITICAL: Critical errors

        Args:
            level (str): The log level (e.g., "INFO", "DEBUG", "WARNING", "ERROR", "CRITICAL").
            message (str): The message to log.
            fileName (str, optional): The name of the log file. By default, it's set to a file in the '_logs_'
                directory with the current date and time as part of the filename.

        Returns:
            None

        Raises:
            Exception: If an error occurs during logging configuration or file I/O, an exception is raised.
                The error message is printed, and the script exits with an error code (7).

        Note:
            - The `get_root_dir_name` function is used to determine the root directory for log file storage.
            - Exceptions that occur during logging configuration or file I/O errors are caught and handled.

        Example:
            # Log an informational message
            logger("INFO", "This is an informational message")

            # Log a warning message
            logger("WARNING", "This is a warning message")
    """
    try:
        logging.basicConfig(level=logging.INFO, filename=fileName, filemode="a",
                            format="%(asctime)-12s %(levelname)s %(message)s",
                            datefmt="%d-%m-%Y %H:%M:%S")

        if level == "INFO":
            logging.info(message)
        elif level == "DEBUG":
            logging.debug(message)
        elif level == "WARNING":
            logging.warning(message)
        elif level == "ERROR":
            logging.error(message)
        elif level == "CRITICAL":
            logging.critical(message)
    except Exception as e:
        print(f"Error: An error occurred while logging: {str(e)}")
        exit(7)
