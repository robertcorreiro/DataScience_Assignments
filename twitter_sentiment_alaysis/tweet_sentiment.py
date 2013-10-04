import sys
import json

def build_sent_dict(filename):
  scores = {}
  for line in filename:
    term, score = line.split("\t")
    scores[term] = int(score)
  return scores
  
def process_tweets(scores, tweet_file):
  contents = tweet_file.readlines()

  for tweet in contents:
    dict = json.loads(tweet)
    if 'text' in dict:
      score = 0
      words = dict['text'].split()
      for word in words:
        if word in scores:
          score += scores[word]
      print score
  

def main():
  sent_file = open(sys.argv[1])
  tweet_file = open(sys.argv[2])
  
  scores = build_sent_dict(sent_file)
  process_tweets(scores, tweet_file)

if __name__ == '__main__':
  main()
