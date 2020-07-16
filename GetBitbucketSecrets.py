import requests
import argparse
import time
import random
import sys

class BitbucketScraper():
    def get_pipeline_secrets(self, args, repo_full_name):
        resp = requests.get( "https://api.bitbucket.org/2.0/repositories/{}/pipelines_config/variables/?page=1&pagelen=100".format(repo_full_name), auth=( args.username, args.password ) ).json()
        if args.debug:
            print( resp.text )
        if args.output == 'default':
            print( "[*]", repo_full_name )
        for k in resp['values']:
            if "value" in k:
                if args.output == 'default':
                    print( k['key'], ":", k['value'] )
                elif args.output == 'csv':
                    print( ",".join( [ repo_full_name, k['key'], k['value'] ] ) )

    def get_repos(self, args):
        page_id = 1
        more_results = True
        while more_results:
            resp = requests.get( "https://api.bitbucket.org/2.0/repositories/{}/?page={}&pagelen=100&fields=values.full_name".format(args.target, page_id), auth=( args.username, args.password ) )
            
            if args.debug:
                print( resp.text )
            if args.output == 'csv':
                print( ",".join( [ "Repo", "Key", "Value" ] ) )

            if resp.status_code == 200:
                resp_json = resp.json()
                for r in resp_json['values']:
                    self.get_pipeline_secrets( args, r['full_name'] )

                if len( resp_json['values'] ) < 100:
                    more_results = False 
                else:
                    page_id = page_id + 1
                    time.sleep( random.uniform( 1, 3 ) ) # be polite
            else:
                print( "[!] Error:", resp.status_code, resp.text )
                sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Extract BitBucket Pipeline Variables and Secrets - @DanAmodio", usage='%(prog)s -t exampleorg -u exampleuser -p examplepassword')
    parser.add_argument("-t", "--target", help="Target Bitbucket org name", required=True)
    parser.add_argument("-u", "--username", help="Login Username (Personal settings > Account settings > Username)", required=True)
    parser.add_argument("-p", "--password", help="Login Password or App Password if 2fa (Personal settings > App passwords)", required=True)
    parser.add_argument("-d", "--debug", help="Enable debug logging", action="store_true")
    parser.add_argument("-o", "--output", help="Output format", default="default", choices=['default', 'csv'])

    args = parser.parse_args()

    bbs = BitbucketScraper()
    bbs.get_repos( args )



if __name__ == '__main__':
    main()


