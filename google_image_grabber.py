from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()
arguments = {"keywords":"CSS Tables" , "limit":200 , "print_urls":False , "chromedriver":"/media/bhams/Stuff/table/dataset/table_images_rename/chromedriver"}
paths = response.download(arguments)