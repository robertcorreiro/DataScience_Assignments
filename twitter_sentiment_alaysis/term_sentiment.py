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
  new_scores = {}

  for tweet in contents:
    dict = json.loads(tweet)
    if 'text' in dict:
      score = 0
      words = dict['text'].split()
      new_terms = []
      for word in words:
        if word in scores:
          score += scores[word]
        else:
          new_terms.append(word)
      for term in new_terms:
        if term not in new_scores:
          new_scores[term] = score
        else:
          new_scores[term] += score
  for w,s in new_scores.items():
    print w, s
      
      

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    scores = build_sent_dict(sent_file)
    process_tweets(scores, tweet_file)
    # lines(sent_file)
    # lines(tweet_file)

if __name__ == '__main__':
    main()
