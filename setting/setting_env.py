def ensure_env_file(env_path):
    try:
        with open(env_path, 'r'):
            print(f"Found existing {env_path} file")
    except FileNotFoundError:
        with open(env_path, 'w') as file:
            print(f"Created new {env_path} file")

def read_lines_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = [line.strip() for line in file 
                    if line.strip() and not line.strip().startswith('#')]
        return lines
    except FileNotFoundError:
        print(f"File {file_path} not found!")

def convert_to_dict(lines):
    result = {}
    for line in lines:
        if '=' in line:
            key, value = line.split('=', 1)
            result[key.strip()] = value.strip()
    return result

def swap_env_values(old_values, new_values):
    old_dict = convert_to_dict(old_values)
    new_dict = convert_to_dict(new_values)

    for key, value in new_dict.items():
        if key in old_dict:
            new_dict[key] = prompt_for_value(key, old_dict[key])
        else:
            new_dict[key] = prompt_for_empty_value(key)

    return new_dict

def prompt_for_value(variable_name, old_value):
    value = input(f"Please enter value for {variable_name}. [Press Enter to set it to the old value: “{old_value}”]: ").strip()
    
    if value:
        return value
    else:
        return old_value
        

def prompt_for_empty_value(variable_name):
    while True:
        value = input(f"Please enter value for {variable_name}: ").strip()
        if value:
            return value
        print("Empty value is not allowed. Please try again.")

def write_env_file(env_path, values):
    with open(env_path, 'w') as file:
        for key, value in values.items():
            file.write(f"{key}={value}\n")

def copy_file_with_prompt(destination_path):
    import shutil
    import os

    while True:
        source_path = input("\nPlease enter the path to your source file: ").strip()
        
        if not source_path:
            print("Empty path is not allowed. Please try again.")
            continue
            
        try:
            # Check if file exists
            if not os.path.isfile(source_path):
                print(f"File not found at '{source_path}'. Please try again.")
                continue
                
            # Copy the file
            shutil.copy2(source_path, destination_path)
            print(f"File successfully copied to {destination_path}")
            return True
            
        except PermissionError:
            print("Permission denied. Please check file permissions and try again.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            print("Please try again.")

def data_from_github(env_path):
    new_env_values_path = '.env.example'
    
    ensure_env_file(env_path)

    old_values = read_lines_from_file(env_path)
    new_values = read_lines_from_file(new_env_values_path)

    return swap_env_values(old_values, new_values)

if __name__ == '__main__':
    env_path = '.env'
    
    while True:
        print("\nPlease choose how to set up your .env file:")
        print("1. Use existing .env file from the system")
        print("2. Fill in values interactively")
        
        choice = input("\nEnter your choice (1 or 2): ").strip()
        
        if choice == "1":
            copy_file_with_prompt(env_path)
            break
        elif choice == "2":
            update_values = data_from_github(env_path)
            write_env_file(env_path, update_values)
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

    print("The .env file is successfully filled!!!")

