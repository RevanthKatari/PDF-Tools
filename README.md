
# PDF Merger Web App

A simple web application built with Streamlit and PyPDF2 to combine multiple PDF files within subfolders into one single PDF file. This app scans a provided root folder, detects subfolders containing PDFs, merges the PDFs within each subfolder, and outputs the combined PDF in the root folder.

## Features
- Automatically detects PDF files within each subfolder.
- Merges PDF files in a specific subfolder in the order of their last modification time.
- Generates a merged PDF for each subfolder with the folder's name as the output PDF file.
- Simple and easy-to-use Streamlit interface.

## Prerequisites

To run this application locally, make sure you have Python installed along with the necessary dependencies.

### Required Libraries
1. **PyPDF2** - Library for manipulating PDF files.
2. **Streamlit** - Library for creating the interactive web interface.

### Install Dependencies

You can install the required libraries using pip:

```bash
pip install PyPDF2 streamlit
```

## Usage

1. Clone or download the repository to your local machine.
2. Place your PDFs in subfolders within a root folder.
3. Open a terminal and navigate to the project directory.
4. Run the Streamlit app with the following command:

```bash
streamlit run app.py
```

5. Once the web app opens, input the path to your root folder in the text input box.
6. Click on the "Combine PDFs" button.
7. The app will process each subfolder containing PDFs, combine them in the order of their modification time, and save the merged PDF in the root folder.
8. After the process is complete, you will see a success message.

## Example Folder Structure

```
root_folder/
    ├── folder1/
    │   ├── file1.pdf
    │   ├── file2.pdf
    ├── folder2/
    │   ├── fileA.pdf
    │   ├── fileB.pdf
    └── folder3/
        ├── fileX.pdf
```

Output: The app will create `folder1.pdf`, `folder2.pdf`, and `folder3.pdf` in the root folder.

## Troubleshooting

- **Invalid Folder Path:** Ensure that the folder path you entered is correct and accessible.
- **Missing Dependencies:** If you receive an error related to missing libraries, make sure all dependencies are installed correctly.

## Contributing

Feel free to open an issue or create a pull request if you encounter any bugs or would like to add new features.

## License

This project is open-source and available under the MIT License.