# File Organizer - Python

A Python script to organize the mess in your downloads folder (or any other folder).

## How to use

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/AdrianHaelisson/Organizador-de-arquivos-python.git
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd Organizador-de-arquivos-python
    ```
3.  **Run the script:**
    ```bash
    python src/file_organizer.py "path/to/your/folder"
    ```
    Replace `"path/to/your/folder"` with the actual path to the directory you want to organize.

## How it works

The script categorizes files based on their extensions and moves them into corresponding folders. The default categories are:

*   PDFs
*   Videos
*   Music
*   Images
*   Documents
*   Archives
*   Executables
*   Other

## Customization

You can customize the file types and extensions by editing the `FILE_TYPES` dictionary in the `src/file_organizer.py` file.