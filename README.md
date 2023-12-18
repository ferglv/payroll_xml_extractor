## Project Overview
`payroll_xml_extractor` is a Python utility designed to parse and extract payroll information from XML files following the SAT (Servicio de Administración Tributaria) standards in Mexico. It supports multiple CFDI versions and converts payroll data into SQL insert statements, facilitating database integration.

## Features
- Supports CFDI versions '3' and '4'.
- Parses employer details, employee positions, payment dates, and deductions from XML files.
- Generates SQL insert statements for database integration.
- Batch processes XML files in a specified directory.

## Requirements
- Python 3.x
- xml.etree.ElementTree module (included in standard Python distribution)

## Installation
No special installation is required. Just ensure Python 3.x is installed on your system.

## Getting Started
Before using `payroll_xml_extractor`, ensure Python 3.x is installed on your system. You can download Python from [here](https://www.python.org/downloads/).

## Usage
To run the project, execute the `main.py` script from the root directory. Ensure that your XML files are placed in the `xml_input` directory.
```bash
python main.py
```

## Project Structure
- src/:
  - xml_parser.py: Contains the core functions for parsing the XML files. It includes functions for extracting namespaces, processing individual XML files, and compiling the data into SQL insert statements.
- xml_input/:
  - Place your XML files in this directory. These files will be processed by the script.
- main.py:
  - The entry point for the application. It calls the functions defined in xml_parser.py to process the XML files.

## Error Handling
The script includes basic error handling for file processing and XML parsing issues. Errors are logged to the console with detailed messages to aid in troubleshooting.

## Limitations
- Tailored for XML files conforming to specific SAT CFDI versions.
- Outputs SQL insert statements to the console; modification may be needed for database integration.

## Notes
- Ensure that the XML files are correctly formatted and adhere to the expected structure for successful parsing.
- The script currently prints the SQL insert statements to the console. Modify the main.py file if you need to redirect this output to a file or a database.

## Troubleshooting
If you encounter issues, check the following:

- Ensure the XML files are in the correct format and version.
- Verify that the file paths in the script are correct.

## Contributions
We welcome contributions! If you'd like to contribute:

- Check for open issues or open a new issue to start a discussion.
- Fork the repository and make your changes.
- Submit a pull request with a clear description of the changes. 

## License
This project is open-source and available under the [MIT License](https://opensource.org/license/mit/).