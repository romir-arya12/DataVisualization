import pandas as pd
import csv
import plotly.graph_objects as go
import plotly.express as px

df=pd.read_csv("data.csv");
studentdf=df.loc[df["student_id"]=="TRL_123"]
print(df.groupby("level")["attempt"].mean())
mean=df.groupby(["student_id","level"],as_index=False)["attempt"].mean()
fig=px.scatter(mean,x="student_id",y="level",size="attempt",color="attempt")
fig.show()