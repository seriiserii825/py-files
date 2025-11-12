def findFile(file_name: str):
    import os

    matches = []
    for root, dirs, files in os.walk("."):
        for file in files:
            if file_name in file:
                matches.append(os.path.join(root, file))
    if matches:
        print("Found files:")
        for match in matches:
            print(match)
    else:
        print("No files found.")
