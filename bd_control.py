import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv('table_.csv')

listr=df['Name']
print(listr)

def search(name):
    result=list()
    df['Name'].apply(lambda x: serch_help(name, df['Name']))
    return result


def serch_help(name, count):
    #print(name,count)
    if name in count:
        
        result.append(df[df['Name']==count])


def main():
    print(search('Авокадо'))
    

main()

