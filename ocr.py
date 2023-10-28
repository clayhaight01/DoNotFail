import easyocr
import os

EASY_OCR_PARAMS = {
    ### TEXT DETECTION PARAMS ###
    'text_threshold': 0.8,  # Text confidence threshold
    'low_text': 0.4,        # Text low-bound score
    'link_threshold': 0.4,  # Link confidence threshold
    'canvas_size': 2560,    # Maximum image size. Image bigger than this value will be resized down.
    'mag_ratio': 1,         # Image magnification ratio
    ### BOUNDING BOX MERGING PARAMS ###
    'slope_ths': 0.5,       # Maximum slope (delta y/delta x) to considered merging. Low value means tiled boxes will not be merged.
    'ycenter_ths': 0.5,     # Maximum shift in y direction. Boxes with different level should not be merged.
    'height_ths': 0.5,      # Maximum different in box height. Boxes with very different text size should not be merged.
    'width_ths':  0.7,       # Maximum horizontal distance to merge boxes
    'add_margin': 0.1,      # Extend bounding boxes in all direction by certain value. This is important for language with complex script (E.g. Thai)
    'x_ths': 2,           # Maximum horizontal distance to merge text boxes when paragraph=True.
    'y_ths': 0.3            # Maximum vertical distance to merge text boxes when paragraph=True
}
reader = easyocr.Reader(['en'], gpu=False, detect_network="craft", recog_network='standard')

def OCR(input_folder):
    with open("marked_text.txt", "w", encoding="utf-8") as outfile:
        files = sorted([f for f in os.listdir(input_folder) if f.endswith(".png")])

        for index, file_name in enumerate(files, start=1):
            img_path = os.path.join(input_folder, file_name)
            result = reader.readtext(img_path, paragraph=True, **EASY_OCR_PARAMS, detail=0)
            
            outfile.write(f"Page {index+1}\n")
            outfile.write("=" * 40)
            outfile.write("\n")

            for detection in result:
                text = detection[1]
                outfile.write(text + "\n")

            outfile.write("\n")
    with open("marked_text.txt", "r", encoding="utf-8") as infile:
        return infile.read()
