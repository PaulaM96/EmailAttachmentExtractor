# EmailAttachmentExtractor

## Description

A tool to automate the extraction of attachments from `.msg` email files, including the extraction of `.zip` files within those attachments. The extracted files are saved to a specified folder for easy access.

## Features

- Extracts attachments from `.msg` email files.
- Automatically extracts `.zip` files contained within the email attachments.
- Saves extracted files to a designated folder.
- User-friendly graphical interface built with Tkinter.

## Installation

### Prerequisites

- Python 3.8 or above.
- Required Python packages are specified in `requirements.txt`.

### Installation Steps

1. Clone the repository and navigate to the project directory.
   1. **Clone the repository and install the required Python packages:**
   ```bash
   git clone https://github.com/your-username/EmailAttachmentExtractor.git
   cd EmailAttachmentExtractor
   pip install -r requirements.txt
   

2. Ensure the correct setup of the extraction paths as per your requirements in the script.

## How to Use

1. Run the application by executing the main script.

2. Using the interface:
   - Click the "Extract Email" button to start processing `.msg` files in the specified directory.
   - The application will automatically extract all attachments, and if any `.zip` files are found, they will also be extracted.
   - A confirmation message will appear once the extraction process is completed.

3. Extracted Files:
   - Extracted files are saved in the folder `\\caminho\ARQUIVOS_EXTRAIDOS`.

## Troubleshooting

- Make sure that the `.msg` files are accessible from the specified directory.
- Ensure that the correct permissions are set for reading the `.msg` files and writing the extracted data.

## Contributing

Feel free to fork the repository, open issues, and submit pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License.
