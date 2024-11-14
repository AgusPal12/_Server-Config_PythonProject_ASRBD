pip install pyinstaller



## Step 1: Install PyInstaller

First, make sure you have PyInstaller installed. You can install it via pip:

    pip install pyinstaller

## Step 2: Make File Paths Relative

Since your app relies on creating and deleting files and folders in the directory where it's executed, you should ensure that paths are relative, so they work no matter where the executable is located (such as on different computers via USB).

For example, instead of using an absolute path, use Python’s os.path module to set paths relative to the directory where the script resides. Update file and folder operations to be relative to the script’s directory:





# Determine base directory dynamically
if getattr(sys, 'frozen', False):
     # Running as an executable
    base_dir = os.path.dirname(sys.executable)
else:
        # Running as a script
    base_dir = os.path.dirname(os.path.abspath(__file__))
# Define main directories relative to base_dir
dir_path = base_dir
path_dossier = os.path.join(base_dir, "Points_de_Restauration")

# Ensure the Points_de_Restauration directory exists
os.makedirs(path_dossier, exist_ok=True)





This way, your program will always create and delete files relative to the script’s location, which will be the USB drive directory when executed from there.

## Step 3: Bundle the Application with PyInstaller

Use PyInstaller to package your app. To ensure it’s fully self-contained, use the following command:

    pyinstaller --onefile --add-data "your_json_folder;your_json_folder" your_script.py

Explanation of Key PyInstaller Flags:

    --onefile: Packages everything into a single executable file.
    --add-data: Specifies extra files or folders to include in the executable. Adjust "your_json_folder;your_json_folder" to add any other folders your app needs. On Windows, use a semicolon (;) to separate source and destination, and on macOS/Linux, use a colon (:).

Example for Windows:

    pyinstaller --onefile --add-data "your_json_folder;your_json_folder" your_script.py

Example for macOS/Linux:

    pyinstaller --onefile --add-data "your_json_folder:your_json_folder" your_script.py

## Step 4: Handling Paths in the Executable

When using --onefile, PyInstaller unpacks the executable into a temporary directory before running. This means you’ll need to modify your code slightly to locate bundled files and folders at runtime.

Add the following snippet to correctly resolve paths within the executable:

    import os
    import sys

    # Determine base directory dynamically
    if getattr(sys, 'frozen', False):
        # Running as an executable
        base_dir = os.path.dirname(sys.executable)
    else:
        # Running as a script
        base_dir = os.path.dirname(os.path.abspath(__file__))

    # Define main directories relative to base_dir
    dir_path = base_dir
    path_dossier = os.path.join(base_dir, "Points_de_Restauration")

    # Ensure the Points_de_Restauration directory exists
    os.makedirs(path_dossier, exist_ok=True)



Replace "." with dir_path:

    Anywhere in your code where you use "." as the path (meaning the current directory), replace it with dir_path.
    This applies to lines where you’re loading or saving JSON files, or where you’re working with files and directories in the current directory.

Replace "./Points_de_Restauration" with path_dossier:

    For any references to "./Points_de_Restauration", replace them with path_dossier.
    This ensures that Points_de_Restauration will be correctly located relative to the executable or script location, whether on a USB or different directories.




This code will dynamically adjust base_dir based on whether the app is running as a regular Python script or a PyInstaller-packed executable.
Step 5: Copy the Executable to USB Drive




Once you’ve created the executable (located in the dist folder), you can copy it to your USB drive. Ensure that any additional folders or files your app needs are also copied to the USB drive in the same structure as they were added with --add-data.
Step 6: Test on Different Machines

Plug your USB into another machine and test the executable. Make sure it can still create, modify, and delete files within the USB directory.

With this setup, your app should work portably from any USB drive and create files and folders relative to the executable location.


pyinstaller --onefile --add-data "Points_de_Restauration;Points_de_Restauration" Gestionnaire-conf_serv.py
















