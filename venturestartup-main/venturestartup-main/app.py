import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import os
import main
col1, col2, col3 = st.columns(3)
with col1:
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')       
        st.header('This is our #2 recommendation.') 
    #if main.resultList[0] == '메이플스토리M':
        img_url = 'https://playgame-img.kakaogames.com/production/images/o7gg-2023-06-08/09-02-36-034/appIcon.png'
        st.image(img_url, caption='메이플스토리M', channels='RGB', width=300)
        st.write(f'''
            <a target="_self" href="https://game.kakao.com/games/KyJPRKvp"> 
                    Redirect to Kakao Game
            </a>
            ''',
            unsafe_allow_html=True,
            # how to make width of button 300px?

        )
    #elif main.resultList[0] == '달빛조각사':
    #    ...
    #elif ...
    #    ...
    #else:
        #raise ValueError('There is no game in the list')
        st.write(f'''
            <a target="_self" href="https://game.kakao.com/games"> 
                 <button type="button" style="width:300px;height:50px;background-color:rgb(255, 255, 255);border: 1px solid rgb(0, 0, 0);border-radius: 5px;">
                    Don't like this game recommendation?
                 </button>
            </a>
            ''',
            unsafe_allow_html=True,
        )    
with col2:
        st.header('This is our #1 recommendation.')
    #if main.resultList[0] == '오딘: 발할라 라이징':
        img_url = 'https://playgame-img.kakaogames.com/production/images/yt5p-2021-06-25/00-19-48-939/appIcon.jpeg'
        st.image(img_url, caption='오딘: 발할라 라이징', channels='RGB', width=300)
        st.write(f'''
            <a target="_self" href="https://game.kakao.com/games/z0Y3ejQ4"> 
                    Redirect to Kakao Game
            </a>
            ''',
            unsafe_allow_html=True,
            # how to make width of button 300px?

        )
    #elif main.resultList[0] == '달빛조각사':
    #    ...
    #elif ...
    #    ...
    #else:
        #raise ValueError('There is no game in the list')
        st.write(f'''
            <a target="_self" href="https://game.kakao.com/games"> 
                 <button type="button" style="width:300px;height:50px;background-color:rgb(255, 255, 255);border: 1px solid rgb(0, 0, 0);border-radius: 5px;">
                    Already playing this game?
                 </button>
            </a>
            ''',
            unsafe_allow_html=True,
        )    
with col3:
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')         
        st.header('This is our #3 recommendation.')    
    #if main.resultList[0] == '오딘: 발할라 라이징':
        img_url = 'https://playgame-img.kakaogames.com/production/images/6081-2022-01-05/16-23-03-877/appIcon.jpeg'
        st.image(img_url, caption='카트라이더 러쉬플러스', channels='RGB', width=300)
        st.write(f'''
            <a target="_self" href="https://game.kakao.com/games/xv5L770n"> 
                    Redirect to Kakao Game
            </a>
            ''',
            unsafe_allow_html=True,
        )
        
    #elif main.resultList[0] == '달빛조각사':
    #    ...
    #elif ...
    #   ...
    #else:
        #raise ValueError('There is no game in the list')
        st.write(f'''
            <a target="_self" href="https://game.kakao.com/games"> 
                 <button type="button" style="width:300px;height:50px;background-color:rgb(255, 255, 255);border: 1px solid rgb(0, 0, 0);border-radius: 5px;">
                    Other game recommendations?
                 </button>
            </a>
            ''',
            unsafe_allow_html=True,
        )    
