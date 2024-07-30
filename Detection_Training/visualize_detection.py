import os
import cv2

# Paths to the folders
image_folder = 'try/Detection_Dataset/Train'
label_folder = 'try/Detection_Dataset/TrainAnno'

# Function to load the labels
def load_labels(label_path):
    with open(label_path, 'r') as file:
        lines = file.readlines()
    boxes = []
    for line in lines:
        parts = line.strip().split(',')
        points = list(map(int, parts[:-1]))
        class_id = parts[-1]
        boxes.append((points, class_id))
    return boxes

# Function to draw bounding boxes on the image
def draw_boxes(image, boxes):
    for box in boxes:
        points, class_id = box
        # Unpack points
        x1, y1, x2, y2, x3, y3, x4, y4 = points
        # Draw the bounding box with lines connecting the points
        cv2.line(image, (x1, y1), (x2, y2), (255, 0, 0), 2)
        cv2.line(image, (x2, y2), (x3, y3), (255, 0, 0), 2)
        cv2.line(image, (x3, y3), (x4, y4), (255, 0, 0), 2)
        cv2.line(image, (x4, y4), (x1, y1), (255, 0, 0), 2)
        # Put the class id near the first point
        cv2.putText(image, str(class_id), (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
    return image

# Main function to visualize images with bounding boxes
def visualize_images(image_folder, label_folder):
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.jpg') or f.endswith('.png')]
    
    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        # Construct the corresponding label file name
        base_name = os.path.splitext(image_file)[0]  # Get the base name without extension
        label_name = f"gt_{base_name}.txt"  # Assuming label names follow this pattern
        label_path = os.path.join(label_folder, label_name)

        if os.path.exists(label_path):
            image = cv2.imread(image_path)
            if image is None:
                print(f"Error loading image {image_file}")
                continue
            boxes = load_labels(label_path)
            image_with_boxes = draw_boxes(image, boxes)

            # Display the image with bounding boxes
            cv2.imshow('Image with Bounding Boxes', image_with_boxes)
            cv2.waitKey(0)  # Wait for a key press to proceed to the next image
            cv2.destroyAllWindows()

# Call the function to visualize images
visualize_images(image_folder, label_folder)
