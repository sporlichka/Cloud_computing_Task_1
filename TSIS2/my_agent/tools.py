import json
import os

def read_file(file_path: str) -> str:
    """Reads the content of a file from the given path.
    
    Args:
        file_path: The path to the file to read.
        
    Returns:
        The content of the file or an error message.
    """
    try:
        # Determine if path is relative, and potentially resolve against a root
        # We try to look in the current directory, and also in the 'my_agent' subdirectory
        # because sometimes execution root varies.
        
        possible_paths = [
            os.path.abspath(file_path),
            os.path.join(os.path.dirname(os.path.abspath(__file__)), file_path),
            os.path.join(os.getcwd(), file_path),
            os.path.join(os.getcwd(), 'my_agent', file_path)
        ]

        target_path = None
        for p in possible_paths:
            if os.path.exists(p):
                target_path = p
                break
        
        if not target_path:
             return f"Error: File '{file_path}' does not exist. Searched in: {possible_paths}"
             
        with open(target_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Error reading file '{file_path}': {e}"

def save_json_result(filename: str, json_content: str) -> str:
    """Saves the JSON analysis result to the JSONS directory.
    
    Args:
        filename: The name of the file to save (e.g., 'analysis_result.json').
        json_content: The JSON string content to write.
        
    Returns:
        Success message or error description.
    """
    try:
        # Define the target directory relative to this tools file
        target_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'JSONS')
        
        # Create directory if it doesn't exist
        os.makedirs(target_dir, exist_ok=True)
        
        # Ensure filename ends with .json
        if not filename.endswith('.json'):
            filename += '.json'
            
        file_path = os.path.join(target_dir, filename)
        
        # If input is a dictionary, serialize it
        if isinstance(json_content, dict):
            content_to_write = json.dumps(json_content, indent=2)
        else:
            # If string, try to re-parse and dump for pretty printing
            try:
                parsed = json.loads(json_content)
                content_to_write = json.dumps(parsed, indent=2)
            except (json.JSONDecodeError, TypeError):
                # If fail, just write the raw string
                # Ensure it's a string
                content_to_write = str(json_content)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content_to_write)
            
        return f"Successfully saved JSON report to {file_path}"
    except Exception as e:
        return f"Error saving JSON file: {e}"
