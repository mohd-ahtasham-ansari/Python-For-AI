import os

# 1. Getting current working directory
current_dir = os.getcwd()
print("1. Current Working Directory:")
print(current_dir)
print("-" * 50)

# 2. Listing files and directories
print("2. Listing files in current directory:")
files = os.listdir(".")
for file in files[:5]:  # print first 5 files/folders
    print(f" - {file}")
print("-" * 50)

# 3. Path manipulations using os.path
print("3. Path manipulation examples:")
# Joining paths correctly regardless of OS (Windows uses \, Mac/Linux uses /)
new_path = os.path.join(current_dir, "test_folder", "sub_folder")
print(f" Joined Path: {new_path}")

# Extracting filename and extension
sample_file = "c:/Users/hp/Desktop/Ai and agents/python for ai/external_tools/rndm.py"
base_name = os.path.basename(sample_file)
dir_name = os.path.dirname(sample_file)
file_name, file_ext = os.path.splitext(base_name)

print(f" Directory name: {dir_name}")
print(f" Base name (file): {base_name}")
print(f" File name only: {file_name}")
print(f" Extension: {file_ext}")
print("-" * 50)

# 4. Checking existence and types
print("4. Checking file existence and types:")
print(f" Does 'external_tools' exist? {os.path.exists('external_tools')}")
print(f" Is 'external_tools' a directory? {os.path.isdir('external_tools')}")
print(f" Is 'main.py' a file? {os.path.isfile('main.py')}")
print("-" * 50)

# 5. Environment Variables
print("5. Environment Variables:")
# Get a common environment variable
path_env = os.environ.get("PATH")
print(f" First 100 characters of PATH env: {path_env[:100]}...")
print("-" * 50)

# 6. Creating and removing directories
print("6. Creating and removing a temporary directory:")
temp_dir = "temp_learning_directory"

if not os.path.exists(temp_dir):
    os.mkdir(temp_dir)
    print(f" Created directory: {temp_dir}")
    
    # Let's create a file inside it
    temp_file_path = os.path.join(temp_dir, "test.txt")
    with open(temp_file_path, "w") as f:
        f.write("Hello, OS library!")
    print(f" Created file inside: {temp_file_path}")
    
    # Verify file exists
    print(f" File exists now? {os.path.exists(temp_file_path)}")
    
    # Cleanup: Remove the file first, then the folder
    os.remove(temp_file_path)
    print(f" Removed file: {temp_file_path}")
    os.rmdir(temp_dir)
    print(f" Removed directory: {temp_dir}")
else:
    print(f" Directory {temp_dir} already exists.")
print("-" * 50)
