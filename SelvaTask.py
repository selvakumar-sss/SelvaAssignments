
# coding: utf-8

# In[14]:

path = "/home/affine/Documents/selva.csv.tar.gz"


# In[20]:

df = sqlContext.read.format('com.databricks.spark.csv').load(path)


# In[21]:

df.printSchema()


# In[25]:

df.columns


# In[19]:

df.show()


# In[38]:

df2 = sqlContext.read.format('com.databricks.spark.csv').options(header = True, inferschema = True, delimeter = ",").load("/home/affine/Documents/selva.csv")


# In[39]:

df2.printSchema()


# In[ ]:




# In[40]:

from pyspark.sql.functions import *
import datetime
from pyspark.sql.types import StringType

def change_date(date):
    date = datetime.datetime.strptime(date, '%Y/%m/%d').strftime('%d/%m/%Y')
    return date
#'%Y-%m-%d'
change_date_udf = udf(change_date, StringType())
df3=df2.withColumn("DOB",change_date_udf(df2.DOB))

df4 = df3.select("name","age","DOB","dept")


# In[41]:

df4.show()


# In[42]:

df4.save


# In[46]:

df4.write.parquet('/home/affine/Documents/selva3')


# In[ ]:



