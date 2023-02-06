import pandas as pd
import re
import matplotlib.colors as mcolors
from sklearn.preprocessing import MultiLabelBinarizer

root = "../../data/external/"

colors = [color[4:] for color in mcolors.TABLEAU_COLORS.keys()]
colors.extend([color for color in mcolors.CSS4_COLORS.keys()])
colors.extend(
    [
        'whitish', 'bluish', 'reddish', 'greenish', 'backish', 'greyish',
        'backish', 'purplish', 'yellowish', 'orangish', 'brownish', 'pinkish'
    ]
)


### PIERRE
file_name = root + 'Dataset_Pierre.csv'
df_Pierre = pd.read_csv(file_name, header=[0, 1]) 
df_Pierre = df_Pierre.iloc[: , 1:]
df_Pierre = df_Pierre.set_index(df_Pierre['Species']['species'])
df_Pierre = df_Pierre.drop(columns=['Species', 'XXX'])


### ANDREI
file_name = root + 'Dataset_Andrei.csv'
df_Andrei = pd.read_csv(file_name)

# Get Dummies to match DF Pierre
df_Andrei_dummies = pd.get_dummies(df_Andrei.iloc[:, 2:])
# Set species back
df_Andrei_dummies = df_Andrei_dummies.set_index(df_Andrei['Species'])

# Create tuple list for multi index
Andrei_multi_index = []
for top_index in df_Andrei.columns:
    for sub_index in df_Andrei_dummies.columns:
        if top_index in sub_index:

            sub_index = sub_index.split('_')[-1]
            Andrei_multi_index.append((top_index, sub_index))

# Set Mutli index
df_Andrei_dummies.columns = pd.MultiIndex.from_tuples(Andrei_multi_index)

### DANIELS
file_name = root + 'Dataset_Kissling.txt'
df_Daniel = pd.read_csv(file_name,
                 sep='\t', encoding='Latin-1')
palm_species = df_Daniel[~df_Daniel.isnull().any(axis=1)]['SpecName'].values
df_Daniel.set_index('SpecName', inplace=True)

# Exclude string types
df_Daniels_int = df_Daniel.select_dtypes(exclude=[object])
df_Daniels_str = df_Daniel.select_dtypes(include=[object])
# Drop numbers
df_Daniels_semi_ints = df_Daniels_int.loc[:, df_Daniels_int.max() <= 3]
# Merge again
df_Daniel_edit = pd.merge(df_Daniels_str, df_Daniels_semi_ints, left_index=True, right_index=True)


# Real numbers:
df_Daniels_real_ints = df_Daniels_int.loc[:, df_Daniels_int.max() >= 3]
columns = [
    ("Measurement", "Maximum Stem Height in Meters"),
    ("Measurement", "Maximum Stem Diameter in Centimeters"),
    ("Measurement", "Maximum Leaf Number"),
    ("Measurement", "Maximum Leaf Blade Length in Meters"),
    ("Measurement", "Maximum Rachis Length in Meters"),
    ("Measurement", "Maximum Petiole Length in Meters"),
    ("Measurement", "Average Fruit Length in Centimeters"),
    ("Measurement", "Minimum Fruit Length in Centimeters"),
    ("Measurement", "Maximum Fruit Length in Centimeters"),
    ("Measurement", "Average Fruit Width in Centimeters"),
    ("Measurement", "Minimum Fruit Width in Centimeters"),
    ("Measurement", "Maximum Fruit Width in Centimeters"),
]

df_Daniels_real_ints.columns = pd.MultiIndex.from_tuples(columns)
df_Daniels_real_ints

# Get colors as lst of lsts 
FruitColorDescription_colors_lst = []

for palm_colors in df_Daniels_str['FruitColorDescription'].values:
    if type(palm_colors) == str:
        #print(type(colors))
        palm_colors = re.split(r'; |to | |-', palm_colors)

        #print(palm_colors)
        FruitColorDescription_colors_lst.append([color for color in palm_colors if color in colors])
    else:
        FruitColorDescription_colors_lst.append([])

MainFruitColors_colors_lst = []

for palm_colors in df_Daniels_str['MainFruitColors'].values:
    if type(palm_colors) == str:
        #print(type(colors))
        palm_colors = re.split(r'; |to | |-', palm_colors)

        #print(palm_colors)
        MainFruitColors_colors_lst.append([color for color in palm_colors if color in colors])
    else:
        MainFruitColors_colors_lst.append([])

# Init SKlearn MLB
mlb = MultiLabelBinarizer()

# Create dummies for color columns
df_FruitColorDescription = pd.DataFrame(
    {
        'FruitColorDescription': FruitColorDescription_colors_lst
    }, columns=['FruitColorDescription'])

s = df_FruitColorDescription['FruitColorDescription']
df_FruitColorDescription = pd.DataFrame(mlb.fit_transform(s),columns=mlb.classes_, index=df_Daniel.index)

# Multiindex columns
columns = [('Fruit Colour Description', column) for column in df_FruitColorDescription.columns]
df_FruitColorDescription.columns = pd.MultiIndex.from_tuples(columns)

# Create dummies for color columns
df_MainFruitColors = pd.DataFrame(
    {
        'MainFruitColors': MainFruitColors_colors_lst
    }, columns=['MainFruitColors'])

s = df_MainFruitColors['MainFruitColors']
df_MainFruitColors = pd.DataFrame(mlb.fit_transform(s),columns=mlb.classes_, index=df_Daniel.index)

# Multiindex columns
columns = [('Fruit Colour', column) for column in df_MainFruitColors.columns]
df_MainFruitColors.columns = pd.MultiIndex.from_tuples(columns)

df_Daniels_str_non_color = df_Daniels_str[['UnderstoreyCanopy', 'FruitSizeCategorical', 'FruitShape', 'Conspicuousness']]

# df_Daniels_str_non_color.columns = pd.MultiIndex.from_tuples(
#     [
#         ('Crown', 'UnderstoreyCanopy'),
#         ('Fruit Size', 'FruitSizeCategorical'),
#         ('Fruit Shape', 'FruitShape'),
#         ('Conspicuousness', 'Conspicuousness'),
#     ]
# )

df_Daniels_str_non_color_dummies = pd.get_dummies(df_Daniels_str_non_color)
columns = []
for column in df_Daniels_str_non_color_dummies.columns:
    level0, level1 = column.split('_')
    if level0 == 'UnderstoreyCanopy':
        level0 = 'Crown'
    elif level0 == 'FruitSizeCategorical':
        level0 = 'Fruit Size'
    elif level0 == 'FruitShape':
        level0 = 'Fruit Shape'
    elif level0 == 'Conspicuousness':
        level0 = 'Conspicuousness'
    columns.append((level0, level1))
    
df_Daniels_str_non_color_dummies.columns = pd.MultiIndex.from_tuples(columns)

### JOIN ALL DATA
data_frames = [df_FruitColorDescription, df_MainFruitColors, df_Daniels_str_non_color_dummies, df_Daniels_real_ints]
df_Daniel_merged = pd.concat(data_frames, axis=1)

### SAVE FILES
root = "../../data/interim/"

df_Daniel_merged.to_csv(root + "DF_Daniel.csv")
df_Andrei_dummies.to_csv(root + "DF_Andrei.csv")
df_Pierre.to_csv(root + "DF_Pierre.csv")