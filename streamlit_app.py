import streamlit
import snowflake.connector
import pandas

streamlit.title('Zena\'s Amazing Athleisure Catalog')

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
                
my_cur.execute("select color_or_style from catalog_for_website")
my_catalog = my_cur.fetchall()

 #put the data into a data frame
df=pandas.DataFrame(my_catalog)
# temp write the dataframe to the page so I can see what I am working with
# streamlit.write(df)
                
 #put the first column into a list
 color_list=df[0].values.tolist()
 #print(color_list)
                
 #Let's put a pick list here so they can pick the color
  option=streamlit.selectbox('Pick a sweatsuit color or style: ',list(color_list))
 #We'll build the image caption now, since we can 
                
 product caption='Our warm, comfortable, '+option+' sweatsuit!'
