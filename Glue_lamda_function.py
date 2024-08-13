import os
import json
import boto3
from botocore.exceptions import BotoCoreError, ClientError, ParamValidationError

glue = boto3.client('glue')

def lambda_handler(event, context):
    # Log the entire event for debugging
    print(f"Received event: {json.dumps(event)}")
    
    # Retrieve the Glue job name from the event
    glue_job_name = event.get('jobname')
    
    # Log the Glue job name for debugging
    print(f"Attempting to start Glue job: {glue_job_name}")
    
    if not glue_job_name:
        return {
            'statusCode': 400,
            'body': json.dumps("Error: 'jobname' is required in the event payload")
        }
    
    try:
        # Start the Glue job
        response = glue.start_job_run(JobName=glue_job_name)
        
        # Log the API response for debugging
        print(f"Glue API Response: {json.dumps(response)}")
        
        # Return a successful response
        return {
            'statusCode': 200,
            'body': json.dumps(f"Glue job started with ID: {response['JobRunId']}")
        }
    except ParamValidationError as error:
        print(f"Parameter validation error: {str(error)}")
        return {
            'statusCode': 400,
            'body': json.dumps(f"Invalid parameters: {str(error)}")
        }
    except (BotoCoreError, ClientError) as error:
        # Log the full error for debugging
        print(f"Full error: {str(error)}")
        print(f"Error type: {type(error).__name__}")
        
        # Extract error message
        if hasattr(error, 'response') and 'Error' in error.response:
            error_message = error.response['Error']['Message']
            print(f"Error response: {json.dumps(error.response)}")
        else:
            error_message = str(error)
        
        # Return an error response
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error starting Glue job: {error_message}")
        }
    except Exception as error:
        # Catch any other unexpected errors
        print(f"Unexpected error: {str(error)}")
        print(f"Error type: {type(error).__name__}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Unexpected error: {str(error)}")
        }