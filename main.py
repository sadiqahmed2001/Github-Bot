import os

def make_commits(days: int):
    if days < 1:
        os.system('git push')
    else:
        date = f'{days} days ago'
        with open('data.txt', 'a') as file:
            file.write(f'{date} <- this was the commit for the day!!\n')

        os.system('git add data.txt')
        os.system(f'git commit --date="{date}" -m "first commit for the day!"')
        make_commits(days - 1)

make_commits(20)
