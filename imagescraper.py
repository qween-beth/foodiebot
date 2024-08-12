import os
from bing_image_downloader import downloader

def download_images(query, num_images=10):
    # Define the directory where images will be saved
    output_dir = 'downloads'
    
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Perform the search and download
    downloader.download(query, limit=num_images, output_dir=output_dir, adult_filter_off=True, force_replace=False, timeout=60)

# Example usage
query = "pineapple fruit"
num_images = 10
download_images(query, num_images)




# import os


# from google_images_download import google_images_download

# def download_images(query, num_images=10):
#     # Create an instance of the google_images_download class
#     response = google_images_download.googleimagesdownload()

#     # Define the arguments for the search
#     arguments = {
#         "keywords": query,
#         "limit": num_images,
#         "print_urls": False,
#         "format": "jpg",
#         "output_directory": "downloads",  # Directory where images will be saved
#         "image_directory": query,  # Sub-directory named after the query
#     }

#     # Perform the search and download
#     paths = response.download(arguments)
#     return paths

# # Example usage
# query = "beef"
# num_images = 10
# download_images(query, num_images)
