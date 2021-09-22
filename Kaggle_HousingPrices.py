from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import RobustScaler, OrdinalEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
import pandas as pd

categorical_features = ["MSZoning",  "Heating", "BldgType", "HouseStyle","Foundation", "GarageType","GarageFinish", "SaleCondition", "SaleType"]
ordinal_features = ["Street", "Alley", "YearBuilt","YearRemodAdd", "ExterQual", "ExterCond", "CentralAir", "GarageYrBlt", "PavedDrive", "YrSold", "MoSold", "FireplaceQu", "HeatingQC", "KitchenQual", "PoolQC"]
numerical_features = ["MSSubClass", "LotFrontage", "LotArea", "OverallQual", "OverallCond", "1stFlrSF", "2ndFlrSF", "FullBath", "HalfBath", "TotalBsmtSF"]

df_train = pd.read_csv("../input/house-prices-advanced-regression-techniques/train.csv")
df_test = pd.read_csv("../input/house-prices-advanced-regression-techniques/test.csv")
train_x = df_train[numerical_features + ordinal_features + categorical_features]
train_y = df_train["SalePrice"]
test_x = df_test[numerical_features + ordinal_features + categorical_features]
# test_y = df_test["SalePrice"] # not available

def recode_likert(df, var_name):
    condition_map =  {"Ex" : 5, "Gd" : 4, "TA" : 3, "Fa" : 2, "Po" : 1, "NA": 0}
    return df.loc[:, var_name].map(condition_map)

df_test.loc[:, "HeatingQC"] = recode_likert(df_test, "HeatingQC")
df_test.loc[:, "FireplaceQu"] = recode_likert(df_test, "FireplaceQu")
df_test.loc[:, "KitchenQual"] = recode_likert(df_test, "KitchenQual")
df_test.loc[:, "PoolQC"] = recode_likert(df_test, "PoolQC")
df_test.loc[:, "BsmtCond"] = recode_likert(df_test, "BsmtCond")

df_train.loc[:, "HeatingQC"] = recode_likert(df_train, "HeatingQC")
df_train.loc[:, "FireplaceQu"] = recode_likert(df_train, "FireplaceQu")
df_train.loc[:, "KitchenQual"] = recode_likert(df_train, "KitchenQual")
df_train.loc[:, "PoolQC"] = recode_likert(df_train, "PoolQC")
df_train.loc[:, "BsmtCond"] = recode_likert(df_test, "BsmtCond")

LandSlope = {"Gtl": 0, "Mod": 1, "Sev":	2}

df_test.loc[:, "LandSlope"] = df_test.loc[:, "LandSlope"].map(LandSlope)
df_test.loc[:, "2ndFlrSF"].fillna(value= 0, inplace=True)

df_train.loc[:, "LandSlope"] = df_train.loc[:, "LandSlope"].map(LandSlope)
df_train.loc[:, "2ndFlrSF"].fillna(value= 0, inplace=True)



numerical_pipeline = Pipeline([
	("imp", SimpleImputer(strategy= "median")),
	("enc", RobustScaler())
])


ordinal_pipeline = Pipeline([ 
	("imp", SimpleImputer(strategy = "constant", fill_value=0)),
	("enc", OrdinalEncoder(handle_unknown = ‘ignore’))
])

categorical_pipeline = Pipeline([
	("imp", SimpleImputer(strategy= "most_frequent")),
	("enc", OneHotEncoder(sparse=True, handle_unknown = ‘ignore’))
])


pre_pipe = ColumnTransformer([
	("cat_pre", categorical_pipeline, categorical_features),
	("ord_pre", ordinal_pipeline, ordinal_features),
	("num_pre", numerical_pipeline, numerical_features)
])

model = sklearn.

full_pipe = Pipeline([
	("pre", pre_pipe),
	("model", model)
])
full_pipe.fit(train_x, train_y)
score = full_pipe.score(test_x, test_y)

y_hat = full_pipe.fit(test_x)

submission = pd.DateFrame()
submission.loc[:, "Id"] = df_test.loc[:, "Id"]
submission.loc[:, "SalePrice"] = y_hat
submission.write_csv("submission.csv")
