import streamlit as st
import pickle
import pandas as pd


df_dict = pickle.load(open('df.pkl','rb'))
df = pd.DataFrame(df_dict)

df['video_id'] = (df['Videourl'].apply(lambda x:x.split('=')[-1]))


def recommend(title):
    video_index = df[df['Title'] == title].index[0]
    dist = simi[video_index]
    video_list = sorted(list((dist)),reverse = True, key = lambda x: x[1])[0:5]
    videos =[]
    vid_id = []
    for i in video_list:  #
        videos.append(df.iloc[i[0]].Title)
        vid_id.append("https://img.youtube.com/vi/{}/hqdefault.jpg".format(df.iloc[i[0]].video_id))
    return videos,vid_id



st.title('Youtube Recommendations')
simi = pickle.load(open('simi1.pkl','rb'))

title = st.selectbox("Select Video",df['Title'])

if st.button("Recommendations"):
    vid_title,vid_id = recommend(title)

    c1,c2 = st.columns(2)
    with c1:
        st.image(vid_id[0])
    with c2:
        st.header(vid_title[0])

    c1, c2 = st.columns(2)
    with c1:
        st.image(vid_id[1])
    with c2:
        st.header(vid_title[1])

    c1, c2 = st.columns(2)
    with c1:
        st.image(vid_id[2])
    with c2:
        st.header(vid_title[2])

    c1, c2 = st.columns(2)
    with c1:
        st.image(vid_id[3])
    with c2:
        st.header(vid_title[3])

    c1, c2 = st.columns(2)
    with c1:
        st.image(vid_id[4])
    with c2:
        st.header(vid_title[4])
