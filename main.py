from src.xml_parser import process_all_xmls


def main():
    """
    The main function to process XML files and extract payroll information.
    """
    directory_path = './xml_input'
    try:
        parsed_data = process_all_xmls(directory_path)
        for data in parsed_data:
            print(data)
    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()
