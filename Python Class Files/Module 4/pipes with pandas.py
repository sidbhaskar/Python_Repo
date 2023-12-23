import pandas as pd

def change_age(x):
    x['age'] = [10,20,30]
    return x
data= {
    'name' : ['Sally','Mary','John'],
    'age' : [50,40,30]
}

df = pd.DataFrame(data)
df.pipe(change_age)
print(df)



