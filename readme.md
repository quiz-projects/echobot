# Deploy the function to the cloud


## Set Environment Variables

The function requires the following environment variables to be set:

- TOKEN: The token to use for the bot
- test: The test to use for the bot

To set the environment variables, run the following commands:

```bash
export TOKEN=<your token>
export test=<your test>
```

## Set webhooks

To set the webhooks, run the following command:

```bash
python setWebhooks.py
```

## Deploy the function

1. Create a deploy script in the root of your project. The script should be named `deploy.sh` and should contain the following:

```bash
gcloud functions deploy echobot \
    --gen2 \
    --region=us-central1 \
    --entry-point=main \
    --runtime=python310 \
    --trigger-http \
    --allow-unauthenticated \
    --set-env-vars=TOKEN=$TOKEN,test=$test
```

- --gen2: Use the new generation of Cloud Functions
- --region: The region to deploy the function to (us-central1 is recommended)
- --entry-point: The name of the function to execute.
- --runtime: The runtime to use for the function (python310 is recommended)
- --trigger-http: The function will be triggered by an HTTP request
- --allow-unauthenticated: The function will be publicly accessible
- --set-env-vars: Set environment variables for the function

To deploy the function, run the following command:

```bash
sh deploy.sh
```

