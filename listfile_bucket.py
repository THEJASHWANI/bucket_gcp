from google.cloud import storage
def upload_file_to_bucket(bucket_name, source_file_name, destination_blob_name):
    # Initialize a client
    storage_client = storage.Client()
    # Get the bucket
    bucket = storage_client.get_bucket(bucket_name)
    # Create a blob and upload the file
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print(f"File {source_file_name} uploaded to {destination_blob_name}.")
def list_files_in_bucket(bucket_name):
    # Initialize a client
    storage_client = storage.Client()
    # Get the bucket
    bucket = storage_client.get_bucket(bucket_name)
    # List all objects in the bucket
    blobs = bucket.list_blobs()
    print("Files in bucket:")
    for blob in blobs:
        print(blob.name)
# Usage
bucket_name = "demo_gcp-1"
source_file_name = "C:/Users/thejashwani/Downloads/from google.py"  # e.g., "sample.txt"
destination_blob_name = "sample1uploaded.txt"  # The name for the file in the bucket
# Upload file
upload_file_to_bucket(bucket_name, source_file_name, destination_blob_name)
# List files
list_files_in_bucket(bucket_name)
