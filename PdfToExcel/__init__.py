import logging
import os 
import io
from azure.storage.blob import BlobServiceClient
import azure.functions as func
from pathlib import Path

conn_str = os.environ["AzureWebJobsStorage"]

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format = "%(asctime)s - %(levelname)s - %(message)s",
    )

def main(myblob: func.InputStream):
    
    setup_logging()
    logging.info(conn_str)
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")
    
    logging.info(f"Checking this if it works")
    p = Path(myblob.name)
    print(p)
    connection_string = os.environ["AzureWebJobsStorage"]
    container_name = "arunakcs"    
    blob_name = myblob.name # Replace with your PDF file name

    # Create a BlobServiceClient object using the connection string
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    # Get a BlobClient object for the PDF file
    blob_client = blob_service_client.get_blob_client(container_name, blob_name)

    # Download the PDF file as a stream
    stream = io.BytesIO()
    blob_client.download_blob().download_to_stream(stream)

    # Use the stream to read the PDF file
    # For example, you could use the PyPDF2 library to extract text from the PDF file
    import PyPDF2
    pdf_reader = PyPDF2.PdfFileReader(stream)
    page = pdf_reader.getPage(0)
    text = page.extractText()

    return func.HttpResponse(f"PDF text: {text}")
    
