import logging
import os 
import io
from azure.storage.blob import BlobServiceClient
import azure.functions as func
from pathlib import Path


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format = "%(asctime)s - %(levelname)s - %(message)s",
    )

def main(myblob: func.InputStream):
    
    setup_logging()
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")
    
    logging.info(f"Checking this if it works")
    
    connection_string = os.environ["AzureWebJobsStorage"]
    container_name = "arunakcs"    
    blob_name = myblob.name # Replace with your PDF file name
    
    logging.info(f"Blob name is {blob_name}")    
    # Create a BlobServiceClient object using the connection string
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    # Get a BlobClient object for the PDF file
    blob_client = blob_service_client.get_blob_client(container_name, blob_name)

    logging.info(blob_client, blob_name)
        
    
