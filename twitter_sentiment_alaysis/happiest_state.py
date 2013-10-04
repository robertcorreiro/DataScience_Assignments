import sys
import json

def build_scores_dict(f):
  "Returns a dict mapping words to scores"
  scores_dict = {}
  for line in f:
    # For tab delimited file
    term, score = line.split("\t")
    scores_dict[term] = int(score)
  return scores_dict
  
def build_states_dict(scores_dict, tweet_file):
  "Returns a dict mapping states to scores"
  tweets = tweet_file.readlines()
  states_dict = {}

  for tweet in tweets:
    dict = json.loads(tweet)

    # Make sure text is in English
    if 'lang' in dict and dict['lang'] == 'en':
      score = 0
      # Sum scores for each word in tweet text
      for word in dict['text'].split():
        if word in scores_dict:
          score += scores_dict[word]
      place = dict['place']
      if place and place['country'] == 'United States':
        # Ex. place['full_name'] returns "Miami, FL"
        state = place['full_name'].split(', ')[1]
        if state not in states_dict:
          states_dict[state] = score
        else:
          states_dict[state] += score
  return states_dict
        
def state_score(pair):
  "For custom sorting by state score"
  return pair[1]

def main():
  sent_file = open(sys.argv[1])
  tweet_file = open(sys.argv[2])

  scores_dict = build_scores_dict(sent_file)
  states_dict = build_states_dict(scores_dict, tweet_file)

  # Custom sorts by largest state score, printing the two letter 
  # abbreviation of the state with the highest score
  states = sorted(states_dict.items(), key=state_score, reverse=True)
  for i in range(5):
    print states[i][0], "=>", states[i][1]

if __name__ == '__main__':
  main()