import urllib.request


def download_image(url, filename):
    try:
        print(f"\nDownloading image...")
        with urllib.request.urlopen(url) as img:
            image = img.read()
            with open(filename, 'wb') as file:
                file.write(image)

        print(f"Image downloaded successfully and saved as {filename}")
    except Exception as e:
        print(f"Error downloading image: {e}")


image_url = input("Enter/Paste image url: ")
# EXAMPLE: 'https://online.umt.edu.pk/img/UMT_Logo.png'
local_filename = 'image.jpg'
download_image(image_url, local_filename)
