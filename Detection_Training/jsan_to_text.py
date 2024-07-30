#actual
import json
import os

def process_json_file(input_file_path, output_file_path):
    """Process JSON file and write output to a text file."""
    with open(input_file_path, "r") as json_file:
        data = json.load(json_file)

        with open(output_file_path, "w") as output_file:
            for value in data["shapes"]:
                points_coordinate = value["points"]
                label = value["label"]
                flat = ",".join(
                    [f"{int(pts[0])},{int(pts[1])}" for pts in points_coordinate]
                )
                joined_output = f"{flat}, {label}"
                output_file.write(joined_output + "\n")

def process_json_files(json_directory, output_directory):
    """Process all JSON files in a directory."""
    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    index = 1
    # Sort filenames based on numeric parts (zero-padded)
    filenames = sorted(os.listdir(json_directory), key=lambda x: int(x.split('.')[0].zfill(10)))
    for filename in filenames:
        if filename.endswith(".json"):
            # Construct file paths
            input_file_path = os.path.join(json_directory, filename)
            output_file_path = os.path.join(output_directory, f"img_{index}.txt")

            # Process JSON file
            process_json_file(input_file_path, output_file_path)

            index += 1

def main():
    """Main function."""
    json_directory = "converted_img/"
    output_directory = "text/"

    try:
        process_json_files(json_directory, output_directory)
        print("Processing completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
