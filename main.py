import streamlit as st
from src import PinterestScraper, PinterestConfig

def download_images(keyword, num_images):
    configs = PinterestConfig(search_keywords=keyword,
                              file_lengths=num_images,
                              image_quality="orig",
                              bookmarks="")
    scraper = PinterestScraper(configs)
    scraper.download_images()

def get_image_urls(keyword, num_images):
    configs = PinterestConfig(search_keywords=keyword,
                              file_lengths=num_images,
                              image_quality="orig",
                              bookmarks="")
    scraper = PinterestScraper(configs)
    return scraper.get_urls()

def main():
    st.title("Pinterest Image Crawler")
    keyword = st.text_input("Enter a keyword:")
    num_images = st.number_input("Number of images to download:", min_value=1, step=1)
    if st.button("Download Images"):
        download_images(keyword, num_images)
        st.success("Images downloaded successfully!")

    if st.button("Get Image URLs"):
        urls = get_image_urls(keyword, num_images)
        st.success("Image URLs retrieved successfully!")
        st.write(urls)

if __name__ == "__main__":
    main()
