import logging
import os 
import io
from azure.storage.blob import BlobServiceClient
import azure.functions as func

conn_str = os.environ["AzureWebJobsStorage"]

def main(myblob: func.InputStream):
    logging.info(conn_str)
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")
    
    logging.info(f"Checking this if it works")
    blob_service_client = BlobServiceClient.from_connection_string(conn_str)
    container_name = myblob.container_name
    blob_name = myblob.name
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    blob_content = blob_client.download_blob().content_as_bytes()
    bytes_io = io.BytesIO(blob_content)
    import PyPDF2
    pdf_reader = PyPDF2.PdfFileReader(bytes_io)
    num_pages  = pdf_reader.getNumPages()
    first_page_text = pdf_reader.getPage(0).extractText()
    # Log the number of pages and the text of the first page
    logging.info(f"Number of pages: {num_pages}")
    logging.info(f"First page text: {first_page_text}")
