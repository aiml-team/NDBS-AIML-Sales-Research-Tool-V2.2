import os

# Define the directory structure
structure = {
    "ai_sales_research": [
        ".env",
        "requirements.txt",
        "app.py",
        {"config": ["__init__.py", "settings.py"]},
        {"models": ["__init__.py", "research_models.py"]},
        {"services": ["__init__.py", "search_service.py", "llm_service.py", "document_service.py"]},
        {"agents": ["__init__.py", "research_agent.py"]},
        {"routes": ["__init__.py", "main_routes.py"]},
        {"templates": ["index.html"]},
        {"utils": ["__init__.py", "logger.py"]}
    ]
}

def create_structure(base_path, items):
    for item in items:
        if isinstance(item, str):
            # Create empty file
            file_path = os.path.join(base_path, item)
            with open(file_path, 'w') as f:
                pass
        elif isinstance(item, dict):
            for folder, sub_items in item.items():
                folder_path = os.path.join(base_path, folder)
                os.makedirs(folder_path, exist_ok=True)
                create_structure(folder_path, sub_items)

# Start creating structure
base_dir = list(structure.keys())[0]
os.makedirs(base_dir, exist_ok=True)
create_structure(base_dir, structure[base_dir])

print(f"Project structure for '{base_dir}' created successfully.")
