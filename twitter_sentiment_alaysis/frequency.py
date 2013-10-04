import sys
import json

def build_freq_dict(filename):
  tweets = filename.readlines()
  freq_dict = {}
  total_words = 0

  for tweet in tweets:
    dict = json.loads(tweet)
    if 'text' in dict:
      for word in dict['text'].split():
        total_words += 1
        if word not in freq_dict:
          freq_dict[word] = 1
        else:
          freq_dict[word] += 1

  for word in freq_dict.keys():
    freq_dict[word] = float(freq_dict[word]) / total_words

  return freq_dict

def get_freq(pair):
  return pair[1]

def main():
  tweet_file = open(sys.argv[1])
  freq_dict = build_freq_dict(tweet_file)

  # Prints the top 20 words
  # words = freq_dict.items()
  # words = sorted(words, key=get_freq, reverse=True)

  # for i in range(20):
  #   print words[i][0], words[i][1]

  for word in freq_dict.keys():
    print word, (float(freq_dict[word])/total_words)

if __name__ == '__main__':
  main()