#EC2 Host information Table
# Author: Jason K Als 

#The goal of this table is to output information regarding of instance's Name, IP and VPC Tag Name the Instance belongs to.  User can filter results based on VPC Id.

#Assumptions made are as follows:
  ## User has Access Key, Secret Key, and Region setup in enviroment Variables 
  ## Table Displays Public IP of the Instance
  ## Code is in Python 3


import os
import sys
import boto3


aws_key = os.environ.get("AWS_ACCESS_KEY_ID")
aws_secret = os.environ.get("AWS_SECRET_ACCESS_KEY")
region = os.environ.get("AWS_EC2_REGION")

vpc_ids = []
vpc_names = []
vpc_match = {}

instance_names = []
instance_ips = [] 
instance_vpcid = []
instance_rows = []

client = boto3.client('ec2', aws_access_key_id=aws_key, aws_secret_access_key=aws_secret, region_name=region)


# Check for valid VPC Ids and save
def checkVPC(**kawrgs):
	response = client.describe_vpcs()
	for i in range(len(response['Vpcs'])):
		if response['Vpcs'][i]['VpcId'] in sys.argv:
			vpc_ids.append(response['Vpcs'][i]['VpcId'])


#Gather instance names, IPs, and VPC tag Names. Put each group of info in its own list
def info():
	boxes = client.describe_instances()
	response = client.describe_vpcs()
	for r in boxes['Reservations']:
		for i in r['Instances']:
			instance_ips.append(i['PublicIpAddress'])
			instance_vpcid.append(i['VpcId'])
			for y in i['Tags']:
				instance_names.append(y['Value'])
	for i in range(len(response['Vpcs'])):
		for vpc_id in vpc_ids:
				if vpc_id in response['Vpcs'][i]['VpcId']:
					vpc_match[vpc_id] = (response['Vpcs'][i]['Tags'][0]['Value'])
	for id in instance_vpcid:
		try:
			vpc_names.append(vpc_match[str(id)])
		except KeyError:
			print('Please enter a valid VPC Id')
			break


#Build table with header and build rows based on information gathered
def table():
	print("----------------------------------------------------------------------")
	print("|    *Instance Name*    |    *Instance IP*    |    *VPC tag Name*    |")
	print("|-----------------------|---------------------|----------------------|")

	for i, x, y in zip(instance_names, instance_ips, vpc_names):
		print("|", i, " " * (20 - len(i)), "|", x, " " * (18 - len(x)), "|", y, " " * (19 - len(y)), "|")

	print("----------------------------------------------------------------------")					

checkVPC()
info()
table()
