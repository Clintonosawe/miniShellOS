Local Model Setup Instructions for miniShellOS

Due to file size constraints, the q4_0-orca-mini-3b.gguf model is not included in this repository.
Follow these steps to download and configure the model on your local machine:

Step 1: Download the Model
---------------------------------
Visit the official GPT4All model page (or your preferred mirror) and download the file:
    q4_0-orca-mini-3b.gguf

Note: The file is approximately 1.98 GB in size.

Step 2: Create the Models Directory
---------------------------------
In the root directory of the miniShellOS project, create a folder named "models".
For example, open your terminal in the project folder and run:
    mkdir -p models

Step 3: Move the Model File
---------------------------------
Move or copy the downloaded model file into the "models" folder.
For example, if the model is in your Downloads folder, run:
    mv ~/Downloads/q4_0-orca-mini-3b.gguf ./models/

Step 4: Verify the File Location
---------------------------------
Ensure that the file is located at:
    miniShellOS-project/models/q4_0-orca-mini-3b.gguf

Step 5: Configure the Application
---------------------------------
The AI helper script (ai_helper.py) is configured to load the model from the "models" folder.
To test the AI integration, activate your virtual environment and run:
    python3 ai_helper.py "Your question here"
For example:
    python3 ai_helper.py "What does the execvp() system call do?"

Important:
---------------------------------
- Do NOT commit the "models" folder to GitHub. The .gitignore file is set up to exclude it.
- Follow these instructions to ensure that your local environment is correctly configured 
  without including the large model file in version control.

