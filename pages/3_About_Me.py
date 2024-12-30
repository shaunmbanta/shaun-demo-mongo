import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="About Me | Shaun Banta"
)

col1, col2 = st.columns(2, gap='small',border=True, vertical_alignment="center")
with col1:
    st.image("objects/shaun-profile.jpeg")
with col2:
    st.write("### About Me")
    """
    Leader at both Google Cloud and in consulting ecosystem focused 
    on growing the surrounding team. 
    
    “A rising tide raises all boats.”
    """
    st.link_button("LinkedIn","https://www.linkedin.com/in/shaunbanta/")
    st.link_button("Review Resume",'objects/Resume - Shaun Banta - Enterprise Account Executive.pdf')

with st.container(border=True):
    st.write("## Work Experience")

    con1 = st.container(border=True)
    con2 = st.container(border=True)
    con3 = st.container(border=True)
    con4 = st.container(border=True)
    #Container 1
    con1.write("### Google, Denver — *GCP Field Sales Representative*")
    con1.write("##### *June 2022 - Present*")
    con1.write("Demonstrated expertise in selling complex cloud solutions to high-growth startups. Achieved significant sales success (150-200% of quota) by leveraging strong technical acumen and strategic partnerships, identifying close opportunities in big data, machine learning, and large language models.")
    #Container 2
    con2.write("### 66 Degreees - *Enterprise Account Executive*")
    con2.write("##### *January 2022 - June 2022*")
    con2.write("Responsible for Google Cloud Platform, Google Workspace, and implementation services sales for 300M-50B+ revenue organizations.")
    #Container 3
    con3.write("### Cloudbakers | Qwinix, Denver — *VP of Sales*")
    con3.write("##### *January 2021 - January 2022*")
    con3.write("Demonstrated strong leadership in building and managing high-performing sales teams. Expertise in go-to-market strategy, sales enablement, and team development. 185% YoY Growth in Implementation Service & Licensing Sales")
    #Container 4
    con4.write("### Cloudbakers, Denver — *Additional Positions Held*")
    con4.write("*Director of Sales (January 2020 - 2021) | 200% YoY Growth*")
    con4.write("*GCP, G Suite & CRM Account Executive (January 2017 - 2020)*")
    con4.write("*Manager of Cloud Enablement & Business Analyst (January 2014 - 2017)*")
    con4.write("*SaaS Deployment Specialist & Implementation Engineer (May 2012 - January 2014)*")

with st.container(border=True):
    st.write("## Education")
    con5 = st.container(border=True)
    con6 = st.container(border=True)

    con5.write("### AltMBA, New York, NY")
    con5.write("##### *January 2016 - May 2016*")
    con5.write("Career enhancement course surrounding multiple aspects of business management fundamentals. Built an eco-friendly business concept to reduce methane emissions.")

    con6.write("### Carroll University, Waukesha, WI — *BS Degree*")
    con6.write("##### *Aug 2008 - May 2012*")
    con6.write("Graphic Communications Major with an emphasis in Web Development.")
    con6.write("Information Systems & Database Architecture Minor.")