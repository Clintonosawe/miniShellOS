miniShellOS Project – README_INSTRUCTIONS.txt

Overview:
-----------
miniShellOS is a custom Unix-like shell developed in C with integrated AI assistance.
The project is a collaborative effort between Clinton Osawe and Ayuub Hagi.
It supports essential shell functionalities such as executing commands, process
management, input/output redirection, and piping. In addition, it integrates a local
AI assistant through a Python script (ai_helper.py) that leverages a GPT4All-based model.
Users can ask technical questions (e.g., "What does the execvp() system call do?") directly
from the shell, and receive AI-generated explanations.

Key Features:
--------------
1. Command Execution and Process Management:
   - Parses and tokenizes user input.
   - Uses fork(), execvp(), and wait() to execute commands in child processes.
2. I/O Redirection and Piping:
   - Supports redirection operators ('>', '<', '>>') to send output to files and read input
     from files.
   - Allows command piping (e.g., "ls -l | less") for chaining command outputs.
3. Command History:
   - Supports recall of previous commands using a history feature (e.g., using "!!").
4. Integrated AI Assistant:
   - Allows users to type "ai 'Your question'" to invoke the AI helper.
   - The Python script (ai_helper.py) uses a local model (q4_0-orca-mini-3b.gguf) via GPT4All
     to generate answers to technical and system programming questions.
   - The large model file is not included in the repository; instructions for downloading and
     setting it up are provided in the MODEL_SETUP.txt file.

System Requirements:
--------------------
- Unix-like operating system (Linux/macOS)
- GCC compiler (GCC >= 7.5.0 recommended)
- Python 3.10+ with a virtual environment set up (venv)
- Required Python packages: transformers, torch, and gpt4all (see requirements.txt if provided)

Installation & Setup:
-----------------------
1. Clone the repository.
2. Create and activate a Python virtual environment:
   $ python3 -m venv venv
   $ source venv/bin/activate
3. Install the required Python packages:
   (venv) $ pip install --upgrade pip
   (venv) $ pip install transformers torch gpt4all
4. Download the q4_0-orca-mini-3b.gguf model file following the instructions in MODEL_SETUP.txt.
   Place the model file in a folder named "models" at the project root.
5. Compile the C code:
   If a Makefile is provided, simply run:
      $ make
   Otherwise, compile manually:
      $ gcc main.c ai_handler.c shell_core.c utils.c -o smartshell

Running the Program:
---------------------
1. Start the shell:
   $ ./smartshell
2. Use standard shell commands (e.g., cd, ls, etc.).
3. To invoke the AI assistant, type:
   ai "What does the execvp() system call do?"
   The shell will call the Python script and display the AI-generated response.
4. Use "!!" to recall and execute the last command.

Troubleshooting:
-----------------
- Ensure that your virtual environment is activated when running ai_helper.py.
- Verify that the model file exists at the correct location: ./models/q4_0-orca-mini-3b.gguf.
- Check that your system has sufficient memory, especially when using larger models.
- If you experience issues with the AI response or model loading, refer to the MODEL_SETUP.txt
  file for instructions on obtaining a compatible model.

Additional Notes:
-----------------
- The venv folder and the models folder are excluded from Git tracking (see .gitignore).
- This project is intended for educational purposes to demonstrate shell programming and
  integration of AI features in a Unix-like environment.

Collaborators:
--------------
- Clinton Osawe
- Ayuub Hagi
