# Short Story Competition
# 06/10/2024

try:
    def start():
        words, lines_per_page, char_per_page = map(int, input().split())
        story = input()

        if story.count(' ') == words - 1 and story.count(' ') != 0:
            print('True')
        else:
            exit()

        start()
    start()
except:
    exit()