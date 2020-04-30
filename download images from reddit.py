import urllib, praw, sys, os

if len(sys.argv) < 4:
    subreddit = raw_input("Enter a subreddit: ")
    user = raw_input("Enter your user agent (I dunno what this is but it's required): ")
    limit = raw_input("Enter limit: ")
else:
    subreddit = sys.argv[1]
    user = sys.argv[2]
    limit = sys.argv[3]
    
fullpath = os.path.abspath(__file__)
dir_path = os.path.dirname(fullpath)
reddit_path = dir_path + "/reddit/"
if not os.path.isdir(reddit_path):
    os.mkdir(reddit_path)
subreddit_path = reddit_path + subreddit + "/"
if not os.path.isdir(subreddit_path):
    os.mkdir(subreddit_path)

r = praw.Reddit(user_agent=user)
my_list = []

posts = r.get_subreddit(subreddit).get_hot(limit=limit)
found = 0
for p in posts:
    found += 1
    my_list.append(p.url)
    print found

downloaded = 0
total_size = 0
image_count = 0
for image in my_list:
    image_count += 1
    print "Finding image #%s" % image_count
    if image.endswith(".jpg") or image.endswith(".png") or image.endswith(".gif"):
        filename = image.split("/")[-1]
        urllib.urlretrieve(image, subreddit_path + filename)
        file_size = os.path.getsize(subreddit_path + filename)
        size_kb = int(file_size) // 1000
        print "Downloaded %s: %dKB" % (filename, size_kb)
        downloaded += 1
        total_size += file_size

mb_size = float(total_size) / 1000000
print "Downloaded %d files, %.2fMB total." % (downloaded, mb_size)