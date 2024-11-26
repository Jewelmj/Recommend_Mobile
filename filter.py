import pandas as pd

#reading the data
def filter():
    df = pd.read_csv('phone_specs.csv')

    #filtering unwanted data
    df = df[(df['Brand'] != 'Black Shark')&(df['Brand'] != 'Micromax')&(df['Brand'] != 'Panasonic')&(df['Brand'] != 'Gionee')&(df['Brand'] != 'Lenovo')&(df['Brand'] != 'Tecno')&(df['Brand'] != 'Yu')&(df['Brand'] != 'Zuk')&(df['Brand'] != 'Meizu')&(df['Brand'] != 'BlackBerry7')&(df['Brand'] != 'Nubia')&(df['Brand'] != 'Google')&(df['Brand'] != 'Huawei')&(df['Brand'] != 'Nokia')]
    df = df[df['Operating system'] == "Android"]
    df = df[df['4G/ LTE'] == "Yes"]
    df = df[df['Processor'] == 8]
    df = df[df['GPS'] == "Yes"]
    df = df[df['Number of SIMs'] == 2]
    df = df[df['3G'] == "Yes"]
    df = df[df['Bluetooth'] == "Yes"]
    df = df[df['Wi-Fi'] == "Yes"]
    df = df[(df['Internal storage (GB)'] == 128.0)|(df['Internal storage (GB)'] == 64.0)  | (df['Internal storage (GB)'] == 256.0) |(df['Internal storage (GB)'] == 512.0)]
    df = df[(df['Rear camera'] == 12)|(df['Rear camera']==16)|(df['Rear camera']==48)|(df['Rear camera']==13)|(df['Rear camera']==64)]
    df = df[df[df.columns[-1]] >=10000]
    df = df.drop(columns=[df.columns[3],df.columns[5],df.columns[6],df.columns[7],df.columns[8],df.columns[9],df.columns[14],df.columns[15],df.columns[16],df.columns[17],df.columns[20]],axis=1)


#making a csv file of the cleaned data
    with open('Phone_specs_new.csv','w') as f:
        df.to_csv(f, sep=',',index=False)

