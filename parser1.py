# python -V
# Python 3.7.1
#
# Usage:
# python parser1.py input_data.txt

import json,  sys
import argparse
from yarl import URL

# Lambda function - check if field is valid or not
# Return ' ' if value is None
checkField = lambda line, propName : '' if line.get(propName)==None else line.get(propName)



# Create main function of program
def main():

  # Create command line parser
  parser = argparse.ArgumentParser(add_help=False)
  parser.add_argument('filename', type=str, help='Set JSON input file, for example: input_data.txt')
  args = parser.parse_args()

  # Get filename from command line
  inp_filename=args.filename

  # Read json to string
  json_data = json.load(open(inp_filename))

  # Output data to STDOUT
  for line in json_data:
   # Create full URL from JSON line
   # In next order:
   #- scheme: string, valid values: http|https
   #- username: an alphanumeric string
   #- password: an alphanumeric string
   #- domain_name: valid domain name
   #- port: integer
   #- path: string
   #- query: Hash with key-value pairs
   #- fragment: string
   #- disabled: boolean
   #
   # How must to be: URL.build(*, scheme, user, password, host, port, path, query, query_string, fragment, encoded=False)
   # New URL generation scheme:
   newURL=URL.build(scheme=line['scheme'], 
   user    =checkField(line, 'username'),
   password=checkField(line, 'password'),
   host    =checkField(line, 'domain_name'),
   port    =checkField(line, 'port'),
   path    ='/'+checkField(line, 'path'),
   query=checkField(line, 'query'),
   fragment=checkField(line, 'fragment')
   )
   # Output to STDOUT generated URL
   print(newURL)

if __name__ == '__main__':                                
  main()