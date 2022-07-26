## aws-metadata-json

## challenge 2 and 3

Challenge2 EC2-Metadata And Get-data-Value from key
Challenge3 Get-Value from nested objects

## Requirement
Get the metadata of ec2 instance within AWS and provide a json formatted output.
A function in which pass the object and a key and get back the value

## How to install
- [Create an EC2 Linux instance on AWS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html)
- [SSH into the instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html)
- Install Python 3 and git on your instance 
    - `sudo yum install python3 git`
- Clone this repository
  - `git clone https://github.com/meetsdeep/-aws-metadata-json-demo.git
- Install pipenv
  - `sudo pip3 install pipenv`
- Open the repository on your instance
  - `cd aws-metadata-json`
- Install project dependancies
  - `pipenv install`


## How to run
- Open the `src` folder
  - `cd aws-metadata-json/src`

## Run Challenge2 Script:

python3 get_ec2_metadata.py
python3 get_data_key.py

Run Challenge3 Script:

python3 get_value.py
`

## How it works
- It makes use of the http://169.254.169.254/latest/meta-data link-local address. Instance metatada is provided at this link, but only when you visit it from a running instance.
- A few simple Python scripts are used to extract the required information using the above API.
- See [AWS user guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html) for more info on the instance metadata API.
