python -m pip install mlflow databricks-cli
$MODEL_PATH = "./model"
$SECURE_TOKEN = ConvertTo-SecureString "$($env:DATABRICKS_TOKEN)" -AsPlainText
$BASE_URI = "$($env:DATABRICKS_HOST)/api/2.0/mlflow"
$MODEL_URI = "$($BASE_URI)/model-versions/get-download-uri"

$PARAMETERS = @{
    name = $env:MODEL_NAME
    version = $env:MODEL_VERSION
}

$response = Invoke-RestMethod -Uri $MODEL_URI  -Body $PARAMETERS -Authentication Bearer -Token $SECURE_TOKEN
dbfs cp -r $response.artifact_uri $MODEL_PATH