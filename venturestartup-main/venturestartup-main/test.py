import pickle
with open('user.pickle', 'rb') as fr:
    user_loaded = pickle.load(fr)

for i in range(len(user_loaded['items'])):
    print(user_loaded['items'][i]['snippet']['title'])
