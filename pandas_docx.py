"""
Pandas:
PANDAS stands for python data analysis library

It is one of the libraries in python.
It works with datasets.
It is useful for analysing,cleaning,exploring and manupulating data.


It allows us to analyse big data and make conclusions based on statistical theories.
Pandas can make clean messy datasets ad mke them readable and relevant.
One of the most preferred and widely used tools in datamunging,wrangling.

Data wrangling:
It is also called data cleaning,dataremediation,data munging.
It regers to a variety of processes designed to transform raw datsa into more readily used formats.


Installation:


Importing:
import pandas 

1.Series:
It is one dimension table.
It takes multiple dat types.

Syntax:
var=pandas.Series([values seperate dby comma])
 we can change index also 
 var=pandas.Seiries([],index=[index names])
 w ecan change dtypes with dtype=typename

 Label:
 we can pass dict to series also
 var=pandas.Series({dict})

 DataFrame:
  It is a 2-d structure.like 2d array table with rows and columnns.
  series+series=DataFrame

  syntax:
  var=pandas.DataFrame([],[],...)
  we can declare index and colmns by
  var=pandas.DataFrame([],[],columns=[],index=[])

  we can make manupulations also and assign it to another col
  ex:
  d4['d']=d4["a"]*d4["b"]

  we can delete one column by pop
  var=pd.pop("column name")  #function

  another way is
  del d3["col name"]  #default

  we can insert one cloumn in between cols of the table
  var=pd.insert(location,colname,assignment values)

  In datafrme also we can pass data  there keys acts as col nmes and vaules became table data

  Head:
  var.head()  #first 5 rows
  var.head(n)  #first n rows

  tail():
  var.tail()  #last 5 rows
  var.tail(n)  #last n rows

  var.info()  #it gives the all info abt table

  sytax:
  
  DataFrame.loc[[start:end],"col name"]
  DataFrame.iloc(row,index)


  DataFrame.isnull()  #check whether null or not and returns true or false
  DtaFrame.isnull().sum #retuns no. of null values
  dataframe.dropna()  #drops the null values row
  dataframe.fillna(value="abc")  #fill yhhe null value with the given value

  When the row headings are repeated we can combine them into one name by groupby

  df.groupby(["colname"]).mean()  #groupby mean

  df.to_csv("data") # for saving
  data=pd.read_csv("data.csv")



  It accepts loop
  by df.iteritems()--> colmn wise loop

  df.iterrows()-->row wise loop

  Dummies:
  df=pd.get_dummies(df["colname])


  Joins:
  we can join 2 tables by joins
  it can be done by merge and we can merge it right or left or inner or outer

  corr():
  it gives the relation betweeen vars
  


  





"""