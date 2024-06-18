import boto3

def lambda_handler(event,context):
    ec2 = boto3.resource('ec2')
    
    for instance in ec2.instance.all():
        state = instance.state['Name']
        if state == 'stopped':
            try:
                instance.start()
            except:
                print("Please fix the error message")