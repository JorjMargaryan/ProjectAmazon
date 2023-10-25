from pathlib import Path

import datetime

from common_.htmlRunner_.sources_ import htmlTestRunner


class HtmlRunner:
    def _get_root_directory(self):
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

    def _generate_report_file_name(self):
        """
            Generate a formatted report file name based on the current date and time.

            This method generates a report file name in the format 'html_report_DD-MM-YYYY_HH-MM-SS.html' based on
            the current date and time. The formatted date and time are obtained using Python's datetime module.

            Returns:
                str: The generated report file name.

            Raises:
                Exception: If an unexpected error occurs while generating the report file name.

            Example usage:
                test_runner = TestRunner()
                report_file_name = test_runner.generate_report_file_name()
                print(f"Generated Report File Name: {report_file_name}")
        """
        try:
            current_datetime = datetime.datetime.now()
            formatted_datetime = current_datetime.strftime('%d-%m-%Y_%H-%M-%S')
            reportFileName = f"html_report_{formatted_datetime}.html"
            return reportFileName
        except Exception as e:
            print(f"Error: An error occurred while generating the report file name: {str(e)}")
            exit(8)

    def get_html_runner(self, title='Test Report', description="Test description"):
        """
            Get an HTMLTestRunner instance for generating test reports.

            This method creates an HTMLTestRunner instance with the specified title and description. It also sets the
            output file for the test report using the current project's root directory and a generated report file name.

            Args:
                title (str, optional): The title of the test report. Default is 'Test Report'.
                description (str, optional): A brief description of the test report. Default is 'Test description'.

            Returns:
                htmlTestRunner.HTMLTestRunner: An HTMLTestRunner instance configured for generating reports.

            Raises:
                Exception: If an unexpected error occurs while creating the HTMLTestRunner instance.

            Example usage:
                test_runner = TestRunner()
                html_runner = test_runner.get_html_runner(title="My Test Suite Report")
                # Now you can use 'html_runner' to run your tests and generate reports.
        """
        try:
            prjRoot = self._get_root_directory()
            outfile = open("{0}\\_reports_\\{1}".format(prjRoot, self._generate_report_file_name()), "wb")
            runner = htmlTestRunner.HTMLTestRunner(
                stream=outfile,
                title=title,
                description=description
            )

            return runner
        except Exception as e:
            print(f"Error: An error occurred while creating HTMLTestRunner: {str(e)}")
            exit(9)
