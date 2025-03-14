from colorama import Fore, Back, Style
import pyfiglet
from PIL import Image
from PIL.ExifTags import TAGS
import os

def extract_image_metadata(image_path):
    if not os.path.exists(image_path):
        print(Fore.RED + "Error: File not found." + Fore.RESET)
        return

    try:
        img = Image.open(image_path)
        exif_data = img._getexif()

        if not exif_data:
            print(Fore.YELLOW + "No EXIF metadata found." + Fore.RESET)
            return

        print(Fore.CYAN + "\n--- Metadata Found ---\n" + Fore.RESET)
        for tag_id, data in exif_data.items():
            tag_name = TAGS.get(tag_id, f"Unknown ({tag_id})")

            # Si el dato es en bytes, lo intentamos decodificar
            if isinstance(data, bytes):
                try:
                    data = data.decode()
                except UnicodeDecodeError:
                    data = "[Binary Data]"

            print(Fore.GREEN + f"{tag_name:25}: " + Fore.WHITE + f"{data}" + Fore.RESET)

    except Exception as e:
        print(Fore.RED + f"Error: {e}" + Fore.RESET)

print("\n\n\n\n\n\n\n\n\n")
print(Fore.GREEN + pyfiglet.figlet_format('Meta - Da t a Scanner'))
print(Fore.LIGHTBLACK_EX + pyfiglet.figlet_format('Made by Konra'))

image_file = input(Fore.WHITE + "Enter the image filename (with extension): " + Fore.RESET)
extract_image_metadata("MetaData/" + image_file)