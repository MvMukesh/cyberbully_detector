# Utilizing-Natural-Language-Processing-to-Detect-Abusive-Language-on-Social-Media
Harnessing the Power of NLP to Cleanse the Social Media Landscape

## Install Required Google Cloud CLI before run : [Click](https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe)

1. Initealize first in CLI, use this command: `gcloud init` give GCP credentials here [it can also be checkedin while completing GCP CLI Setup]
2. Provide Project Name, Select Compute Resion 
3. Create a Bucket with unique name (to save data)
4. Upload data in the Bucket (simple drag and drop csv file from local to new bucket)

<p align="center">
  <kbd><img src="https://github.com/MvMukesh/Utilizing-Natural-Language-Processing-to-Detect-Abusive-Language-on-Social-Media/assets/26667491/1d01f863-ff3f-4612-b92f-0923b373689b" alt="gcp.png"></kbd>
</p>

`NOTE:` 
* There are plethora of tutorials on how to setup GCP CLI
* Don'r forget to add artifacts in git ignore

---

<h2><u>Data Ingestion</u></h2>
<p align="center">
  <kbd><img src="https://github.com/MvMukesh/Utilizing-Natural-Language-Processing-to-Detect-Abusive-Language-on-Social-Media/assets/26667491/a45ad982-e0ec-47e0-8409-36c3a51e94b8" width=700 height=700 alt="data ingestion.png"></kbd> 
</p>
Imagine you're a chef preparing a delicious dish. This data pipeline is like your kitchen helpers and recipe steps, transforming raw ingredients (data) into a tasty meal (insights)!

1. `Gathering Ingredients`:

* We have various suppliers (data sources) like text files, databases, or even zipped bags (zip files) full of data.
* We first unpack any zipped bags in the "unzip_and_clean" step to make sure everything is accessible.
* Then, we set up our kitchen workstations (new directories) to keep things organized.

2. `Preparing the Feast`:

* This is where the real cooking starts! We clean and chop the ingredients (data preparation).
* This might involve removing unwanted parts, cutting them into smaller pieces (e.g., words from sentences), or even bringing in special seasoning (pretrained model weights, if needed).
* We follow a specific recipe (data ingestion) that involves tasks like transforming the data into formats our model understands and maybe even cooking with pre-trained flavors (model loading).

3. `Serving Delicious Outcome`:

* Finally, the finished dish (processed data)! This could be predictions from our model, like predicting sentiment, or neatly prepared data files ready for further analysis.
* We serve this tasty output to hungry customers (models or analysts) who can use it to make informed decisions or create even more insights.

**`Remember`:**

* The order of some steps might be flexible depending on our recipe (implementation).
* Some details might be hidden like specific cleaning techniques or seasoning ingredients, but the overall flow remains the same.


<h2><u>Data Transformation</u></h2>
<p align="center">
  <kbd><img src="https://github.com/MvMukesh/Utilizing-Natural-Language-Processing-to-Detect-Abusive-Language-on-Social-Media/assets/26667491/a89966ca-f1b5-4d65-b553-17cdbdcb265a" width=700 height=700 alt="data transformation.png"></kbd> 
</p>

<h2><u>Model Training</u></h2>
<p align="center">
  <kbd><img src="https://github.com/MvMukesh/Utilizing-Natural-Language-Processing-to-Detect-Abusive-Language-on-Social-Media/assets/26667491/ed9a046e-848d-4233-8af9-62546215ec41" width=700 height=700 alt="model training.png"></kbd> 
</p>

Remaining Pipelines to Add: Model Evaluation and Model Push Back to GCP
