# Setup Project

This document provides a step-by-step guide to setting up the project locally.

## Steps

1. **Pull Project**
   - Clone the repository to your local machine using Git.

2. **Add .env File**
   - Create a `.env` file in the root directory.
   - Include the necessary Supabase URL and key:
     ```plaintext
     SUPABASE_URL=<your_supabase_url>
     SUPABASE_KEY=<your_supabase_key>
     ```

3. **Create Python Virtual Environment**
   - Set up a virtual environment to isolate dependencies.
   
   **Command:**
   ```bash
   py -m venv <env_name>
   <env_name>/Scripts/activate

4. **Install python libraries**
   - 
   
   **Command:**
   ```bash
   pip install -r requirements.txt

5. **Run chalice locally**
   -
    **Command**
    ```bash
    chalice local