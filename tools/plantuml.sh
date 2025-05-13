#!/bin/bash

# Define the function
render() {
    echo "--------Rendering PlantUML diagram...--------"

    # Arguments
    FOLDER_NAME="$1"
    FILE_NAME="$2"

    # Build the absolute path to the docs directory
    DOCS_DIR="../docs"
    DOCS_ABS_DIR=$(realpath "$DOCS_DIR")

    echo "Doc abs path: $DOCS_ABS_DIR"
    echo "Folder: $FOLDER_NAME"
    echo "File: $FILE_NAME"

    # Run PlantUML Docker container, pointing to the file in the correct path
    docker run --rm -v "${DOCS_ABS_DIR}:/docs" plantuml/plantuml "/docs/$FOLDER_NAME/$FILE_NAME"
    echo ""
}

render_all(){
    # List of folders to process
    FOLDERS=(
        "architecture"
        "cicd"
    )

    # Loop through each folder and render each .puml file
    for folder in "${FOLDERS[@]}"; do
        for file in ../docs/"$folder"/*.puml; do
            # Get the file name only, without path
            file_name=$(basename "$file")
            render "$folder" "$file_name"
        done
    done
}

main() {
    # render architecture diagram.puml
    render_all
}

main