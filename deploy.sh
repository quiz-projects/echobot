gcloud functions deploy echobot \
    --gen2 \
    --region=us-central1 \
    --entry-point=main \
    --runtime=python310 \
    --trigger-http \
    --allow-unauthenticated