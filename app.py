import pandas as pd
import streamlit as st
import numpy as np
st.title('Clinical Informatics Fellowship Application Tool')
st.write('7/14/2020 *version 1.2*')
st.markdown('by *Chengda Zhang, MD*')
data=pd.read_csv('CI fellowship database.csv')
data=data.set_index(['Programs'])

st.markdown('Instruction: This app will tell you what documents you will need to apply for selected clinical informatics fellowships. Please select your target application area/programs on the left.')
options = st.sidebar.multiselect(
     'What are your targeted area',
        tuple(set(data['Region'])))

programs = st.sidebar.multiselect(
    'Your targeted area include the following programs, you can modify by program here',
    tuple(data[data['Region'].isin(options)].index),
    default=list(data[data['Region'].isin(options)].index))


#dfoptions=pd.DataFrame(options)
#dfoptions.columns=['You selected']
#dfoptions.index=dfoptions.index+1
#st.write(dfoptions)
if (len(programs)==0):
    st.write('*Please make your selection on the left*')
else:
        
    selected_data=data.loc[data.index.isin(programs)]
    for column in selected_data.columns:
        for index in selected_data.index:
            if selected_data.loc[index,column]==True:
                selected_data.loc['Summary',column]=True

  #  st.header("Programs you have selected")
   # st.map(selected_data[["lat", "lon"]].dropna(how="any"))

    if True not in list(selected_data.loc['Summary'][4:]):
        st.write('*The application requirement is not readily available on internet for all your selected programs, please contact the programs.*')
    else:

        #st.write('All of selected programs participate in ERAS. The application start in July.')
        st.write('**Based on your selection, you will need to submit the following documents to apply for selected programs:**')
        checklist=list()
        for column in selected_data.columns[5:]:
            if selected_data.loc['Summary',column]==True:
                checklist.append(column)

        required=pd.DataFrame(checklist)
        required.columns=['Required documents']
        required.index=required.index+1
        st.write(required)
        lor=selected_data['Letters of recommendation'].dropna()
        #st.write(lor)
        if len(lor)==0:
            st.write('There is not enough information regarding how many letters of recommendation you will need, please contact the program.')
        else:
            st.markdown('You will need %i letters of recommendations (including PD and CI attending letters if required)' % max(lor))

        #st.write(selected_data['Participating ERAS'])

        if False in list(selected_data['Participating ERAS']):
            st.write('The following programs does not participate in ERAS, please contact the program for more information:')
            st.write(selected_data[selected_data['Participating ERAS']==False].index)

        if 'Yes' in list(selected_data['Pathology graduates only']):
                st.write('The following programs ONLY accept pathology graduates:')
                st.write(selected_data[selected_data['Pathology graduates only']=='Yes'].index)

        if st.checkbox("Show specific data for each program", False):
            st.subheader('specific data for each program')
            st.write(selected_data.iloc[:-1,0:16])
st.markdown(' ')
st.markdown(' ')
st.markdown('This app is created mainly for non-pathology graduates, while all programs (pathology and non-pathology based) are included, some program may not accept pathology graduates. Please check with the programs.')
st.markdown('Data is extracted from FREIDA, AMIA, ERAS and program websites. No new updates were found in ERAS since its opening in 6/2020. Please contact me at zhangcd07@outlook.com with questions.')       