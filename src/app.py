## Setting up Cohere

import cohere
co = cohere.Client('YOUR_COHERE_API_KEY')

# Example of using a Cohere API method
response = co.summarize(
    text = 'text')

print(response)