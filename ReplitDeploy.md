# Replit Deployment Instructions

To deploy your Streamlit application to Replit, please follow these steps:

1.  **Create a New Repl:**
    *   Go to [Replit.com](https://replit.com/), log in, and create a new Repl.
    *   Select the "Python" template.

2.  **Upload Your Files:**
    *   Once your Repl is created, upload your project files (`app.py`, `requirements.txt`, and any other necessary files or folders) to the root directory of your new Repl.

3.  **Configure `.replit` file:**
    *   In your Replit environment, locate the `.replit` file. If it doesn't exist, you can create it.
    *   Edit the `.replit` file to contain the following line:
        ```
        run = "streamlit run app.py"
        ```
    *   This line tells Replit how to execute your Streamlit application when you click the "Run" button.

4.  **Install Dependencies:**
    *   Replit usually detects your `requirements.txt` file and automatically installs the listed dependencies.
    *   If the dependencies are not installed automatically, open the "Shell" tab within your Replit environment and run the following command:
        ```bash
        pip install -r requirements.txt
        ```

After completing these steps, your Streamlit application should be successfully deployed and running on Replit.