import os

def makecommits(days : int):
    if days < 1:
        os.system('git push')
    else:
        dates =f'{days} days ago'
        with open('data.txt','a') as file:
            file.write(f'{dates}<- this was the commit for the day!!\n')

            os.system('git add data.txt')

            os.system('git commit --date="'+dates +'" -m "first commit for the day!"')
            return days * makecommits(days -1)
        
makecommits(665)