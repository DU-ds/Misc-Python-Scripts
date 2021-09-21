from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import RobustScaler, OrdinalEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
import pandas as pd

recode:
LandSlope = {"Gtl": 0, "Mod": 1, "Sev":	2}
df.loc[:, "LandSlope"] = df.loc[:, "LandSlope"].map(LandSlope)
df.loc[:, "2ndFlrSF"].fillna(value= 0, inplace=True)


def recode_likert(df, var_name):
	condition_map =  {"Ex" = 5, "Gd" = 4, "TA" = 3, "Fa" = 2, "Po" = 1, "NA": 0}
	return df.loc[:, var_name].map(condition_map)

df.loc[:, "HeatingQC"] = recode_likert(df, "HeatingQC")
df.loc[:, "FireplaceQu"] = recode_likert(df, "FireplaceQu")
df.loc[:, "KitchenQual"] = recode_likert(df, "KitchenQual")
df.loc[:, "PoolQC"] = recode_likert(df, "PoolQC")
categorical_features = ["MSZoning",  "BldgType", "HouseStyle","Foundation", "GarageType","GarageFinish", "SaleCondition", "SaleType"]

ordinal_features = ["Street", "Alley", "YearBuilt","YearRemodAdd", "ExterQual", "ExterCond", "CentralAir", "HeatingQC", "GarageYrBlt" "PavedDrive", "YrSold", "MoSold", "FireplaceQu", "HeatingQC", "KitchenQual", "PoolQC"]

# recode LandContour: Bnk = 1, HLS = 1, Lvl = 0, Low = -1

numerical_features = ["MSSubClass", "LotFrontage", "LotArea", "OverallQual", "OverallCond", "1stFlrSF", "2ndFlrSF", "Bedroom", "FullBath", "HalfBath"]

df_test = pd.read_csv("")
df_train = pd.read_csv("")

train_x = df_train[numerical_features + ordinal_features + categorical_features]
train_y = df_train["SalePrice"]
test_x = df_test[numerical_features + ordinal_features + categorical_features]
test_y = df_test["SalePrice"]


numerical_pipeline = Pipeline([
	("imp", SimpleImputer(strategy= "median")),
	("enc", RobustScaler)
])


ordinal_pipeline = Pipeline([ 
	("imp", SimpleImputer(strategy = "constant", fill_value=0)),
	("enc" OrdinalEncoder()))
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

model = sklearn

full_pipe = Pipeline([
	("pre", pre_pipe),
	("model", model)
])
full.fit(train_x, train_y)
score = full.score(test_x, test_y)

y_hat = full.fit(test_x)

submission = pd.DateFrame()
submission.loc[:, "Id"] = df_test.loc[:, "Id"]
submission.loc[:, "SalePrice"] = y_hat
submission.write_csv("submission.csv")
