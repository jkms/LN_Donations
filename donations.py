#!/usr/bin/python3
import pandas as pd
import argparse


#argument stuff
parser = argparse.ArgumentParser()
parser.add_argument("-l", "--leadnow", help="the leadnow csv", type=str)
parser.add_argument("-d", "--donation", help="the donation csv", type=str)
parser.add_argument("-o", "--outfile", help="the output csv", type=str)
args = parser.parse_args()

if __name__ == "__main__":
     # Read the file
     donations = pd.read_csv(args.donation, low_memory=False)
     leadnow = pd.read_csv(args.leadnow, low_memory=False)
     
     # Output the number of rows
     print("Total rows: {0}".format(len(donations)))
     
     # change everything to uppercase, and remove all whitespaces.
     # print(list(donations)) #Display headers
     leadnow['postcode'] = leadnow['postcode'].str.upper()
     leadnow['postcode'] = leadnow['postcode'].str.replace(' ', '')
     leadnow['last_name'] = leadnow['last_name'].str.upper()
     leadnow['last_name'] = leadnow['last_name'].str.replace(' ', '')
     leadnow['first_name'] = leadnow['first_name'].str.upper()
     leadnow['first_name'] = leadnow['first_name'].str.replace(' ', '')
     donations['Contributor last name'] = donations['Contributor last name'].str.upper()
     donations['Contributor last name'] = donations['Contributor last name'].str.replace(' ', '')
     donations['Contributor first name'] = donations['Contributor first name'].str.upper()
     donations['Contributor first name'] = donations['Contributor first name'].str.replace(' ', '')
     
     
     new_df = pd.merge(leadnow, donations,  how='left', left_on=['last_name','first_name','postcode'], right_on = ['Contributor last name','Contributor first name','Contributor Postal code'])
     print(new_df[list(leadnow) + ['Recipient', 'Contribution Received date', 'Monetary amount']])
     new_df.to_csv(args.outfile, sep='\t')

