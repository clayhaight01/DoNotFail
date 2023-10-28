import easyocr
import os

reader = easyocr.Reader(['en'], gpu=False, detect_network="craft", recog_network='standard')

def OCR(input_folder):
    with open("marked_text.txt", "w", encoding="utf-8") as outfile:
        files = sorted([f for f in os.listdir(input_folder) if f.endswith(".png")])

        for index, file_name in enumerate(files, start=1):
            img_path = os.path.join(input_folder, file_name)
            result = reader.readtext(img_path)
            
            outfile.write(f"Page {index+1}\n")
            outfile.write("=" * 40)
            outfile.write("\n")

            for detection in result:
                text = detection[1]
                outfile.write(text + "\n")

            outfile.write("\n")
    with open("marked_text.txt", "r", encoding="utf-8") as infile:
        return infile.read()
