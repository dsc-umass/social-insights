import requests
import base64
import json


class TwitterScraper:

    def __init__(self):

        self.auth_token_path = "twitter_tokens.txt"
        self.base_url = "https://api.twitter.com/"

        self.tokens_dict = self.get_tokens()
        self.access_token = self.tokens_dict["access_token"]

        self.search_headers = {'Authorization': 'Bearer {}'.format(self.access_token)}



    def search_tweets_by_keyword(self, keyword, result_type = "recent", count = 1, max_results = 500):

        search_url = '{}1.1/search/tweets.json'.format(self.base_url)

        search_params = {
            'q': "\"" + str(keyword) + "\"",
            'result_type': result_type,
            'count': count,
            'maxResults': max_results
        }

        resp = requests.get(search_url, params=search_params, headers=self.search_headers)

        if resp.status_code != 200:

            print("The request failed with error code: " + resp.status_code + "\n")

            return False


        else:
            status_list = resp.json()["statuses"]

            next_url = self.base_url + resp.json()["search_metadata"]["next_results"]

            status_list.extend(self.search_by_url(next_url, search_params, "statuses"))
            return status_list


    def search_by_url(self, url, params, key = None):

        
        response = requests.get(url, params)

        if response.status_code != 200:

            print("failed")
            print(response.status_code)
            exit()

        elif key == None:
            
            return response.json()

        else:
            full_response = response.json()
            requested = full_response[key]
            if "next_results" in full_response["search_metadata"]:
                
                url = self.base_url + full_response["search_metadata"]["next_results"]
                requested.extend(self.search_by_url(url, params, key))
                return(requested)
            
            return requested


    def get_tokens(self):

        token_dict = {}
        token_file = open(self.auth_token_path, 'r')

        for line in token_file:

            line = line.rstrip()
            parsed_line = line.split(': ')

            token_dict[parsed_line[0]] = parsed_line[1]

        token_file.close()

        return token_dict


    def reset_tokens_dict(self):

        self.key_secret = '{}:{}'.format(
            self.tokens_dict["consumer_key"], 
            self.tokens_dict["consumer_secret"]).encode('ascii')

        b64_encoded_key = base64.b64encode(self.key_secret)
        b64_encoded_key = b64_encoded_key.decode('ascii')

        auth_headers = {
            'Authorization': 'Basic {}'.format(b64_encoded_key),
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
        }
        auth_data = {
            'grant_type': 'client_credentials'
        }

        auth_url = '{}oauth2/token'.format(self.base_url)
        auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)

        self.tokens_dict['access_token'] = auth_resp.json()['access_token']



    def write_tokens(self):

        token_file = open(self.auth_token_path, 'w')

        for key in self.tokens_dict.keys():

            token_file.write("{}: {}\n".format(key, self.tokens_dict[key]))
        
        token_file.close()



def main():

    ts = TwitterScraper()
    tweets = ts.search_tweets_by_keyword("Example Text", count = 100)
    status_1 = tweets
    
    print(json.dumps(status_1, indent = 4))
    print(len(tweets))
        

if __name__ == "__main__":

    main()
