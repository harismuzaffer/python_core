def get_max_twitters_ordered_by_username(username_count_map):
    """
    username_count_map: A dict with key as the username and 
    value as the no. of tweets

    return: A list - all those twitters with max number of tweets. Each item of
    this list is a dic with key as the user_name and value as the no. of tweets
    """
    max_number_of_tweets = max([i for i in username_count_map.values()])

    # list of twitters with max tweets i.e. those having tweets equal to 
    # max_number_of_tweets
    max_twitters_list = [{k: v} 
                         for k, v in username_count_map.items() 
                         if v == max_number_of_tweets]

    # sort max_twitters_list based on the user_name i.e. alphabatically
    sorted_max_twitters_list = sorted(max_twitters_list, key=lambda x: list(x.keys()))

    return sorted_max_twitters_list

def get_max_twitters():
    """
    For every test case
        1: Build a dictionary of usernames and no. of tweets by the usernames
        2: Get twitters with max number of tweets ordered by the username 
        alphabatically

    Return: A list of twiters with max number of tweets. Each item of the list
    is a dict whose key is the username and value is the number of tweets
    """
    # number of test cases
    t = int(input())
    max_twitters = []
    for _ in range(t):
        # number of tweets corresponding to the test case
        number_of_tweets = int(input())

        # A dict whose key is a user_name and value is the number of tweets 
        # corresponding to the user_name
        username_count_map = {}

        # builds the username_count_map dictionary
        for _ in range(number_of_tweets):
            tweet_object = input()
            user_name = tweet_object.split(' ')[0]
            if username_count_map.get(user_name):
                username_count_map[user_name] += 1
            else:
                username_count_map[user_name] = 1

        twitters_with_max_tweets = get_max_twitters_ordered_by_username(username_count_map)
        max_twitters.extend(twitters_with_max_tweets)

    return max_twitters

if __name__ == '__main__':
    """
    1: Get the list of twitters with max number of tweets
    2: Print their username and number of tweets
    """
    max_twitters_list = get_max_twitters()
    for item in max_twitters_list:
        user_name = list(item.keys())[0]
        number_of_tweets = list(item.values())[0]
        print(user_name, number_of_tweets)

