## Helpfull in getting and pussing data to GCP

import os

class GCloudSync:

    #method to push from local to gcp
    def sync_folder_to_gcloud(self, gcp_bucket_url, filepath, filename):
        command = f"gsutil cp {filepath}/{filename} gs://{gcp_bucket_url}/"
        # command = f"gcloud storage cp {filepath}/{filename} gs://{gcp_bucket_url}/"
        os.system(command)

    #method to download in local from gcp
    def sync_folder_from_gcloud(self, gcp_bucket_url, filename, destination):
        command = f"gsutil cp gs://{gcp_bucket_url}/{filename} {destination}/{filename}"
        # command = f"gcloud storage cp gs://{gcp_bucket_url}/{filename} {destination}/{filename}"
        os.system(command)

                                 ### ---- Manralai.in ---- ### 
## Install Google Cloud CLI before run : https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe