from dataclasses import field
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import datetime

# page setup
st.set_page_config(
    layout="wide"
)

# 1. loading datasets
data = pd.read_csv('data/oh-counties.csv', encoding='utf-8')
data['date'] = pd.to_datetime(data['date'])
counties = ['All counties'] + list(data['county'].unique())

osu_data = pd.read_csv('data/osu-cases.csv', encoding='utf-8')
osu_data['date'] = pd.to_datetime(osu_data['date'])

vacci_data = pd.read_csv(
    'data/Ohio State Vaccination Summary.csv', thousands=',', encoding='utf-8')
vacci_data['value'] = pd.to_numeric(vacci_data['value'])

vacci_rate = str(round(
    vacci_data.at[0, 'value'] / (vacci_data.at[0, 'value'] + vacci_data.at[1, 'value']), 2))

# interface

# search hex color
st.markdown("<div style='background:#e6e6e6'><h3 style='font-weight:bold; color:#ac2217'>COVID-19 dashboard</h3></div>", unsafe_allow_html=True)

ohio_panel = st.container()

with ohio_panel:

    columns = st.columns([2, 0.2, 2.1, 0.2, 1.2, 0.2, 1.2])

    with columns[0]:

        start_time = st.slider("select the date",
                               data['date'].min().date(),
                               data['date'].max().date(),
                               data['date'].max().date()
                               )

        current_data = data.loc[data['date'] == pd.to_datetime(start_time)]

        county = columns[2].selectbox(
            'County',
            (counties),
            key="county"
        )

        if county == 'All counties':
            county_data = data.groupby('date').sum().reset_index()
        else:
            county_data = data.loc[data['county'] == county]


        timespan = columns[4].radio(
            'Time',
            ('All Time', 'Last 90 Days')
        )

        max_date = data['date'].max()
        past_90_date = max_date - datetime.timedelta(days = 90)

        if timespan == 'All Time':
            filter_data = county_data
        else:
            filter_data = county_data.loc[county_data['date'] > past_90_date]


        daily_type = columns[6].radio(
            'Type',
            ('daily_cases', 'daily_deaths')
        )

    chart1, chart2 = st.columns([1,2])

    with chart1:

        url = "https://raw.githubusercontent.com/deldersveld/topojson/master/countries/us-states/OH-39-ohio-counties.json"

        oh_state = alt.topo_feature(url, "cb_2015_ohio_county_20m")


        OH_map = alt.Chart(oh_state).mark_geoshape(stroke='lightgray').encode(
            color=alt.Color('cases:Q'),
            tooltip=['county:N', 'cases:Q']
        ).transform_lookup(lookup='properties.NAME',from_=alt.LookupData(current_data, 'county', list(current_data.columns))).project(
            type='albersUsa'
        )

        st.altair_chart(OH_map, use_container_width = True)

    with chart2:

        line = alt.Chart(filter_data).mark_line().encode(
            x = alt.X('date:T'),
            y = alt.Y(daily_type),
            tooltip = ['date', daily_type]
        ).properties(
            title = daily_type + ' in ' + county
        ).interactive(
            bind_y = False
        )

        st.altair_chart(line, use_container_width = True)

osu_panel = st.container()

with osu_panel:

    columns = st.columns([1, 4, 1])

    with columns[0]:

        st.markdown("<div style='background:#e6e6e6; text-align: center;'><span style='color: #ac2217; font-weight:bold'>Last 7 Days</span></div>", unsafe_allow_html=True)

        st.markdown("<div style='text-align: center;'><span style='color: #000000; font-size:1.5rem; font-weight:bold'>Cases</span></div>", unsafe_allow_html=True)

        st.markdown("<div style='text-align: center;'><span style='color: #681a49; font-size:1.5rem; font-weight:bold'>7</span></div>", unsafe_allow_html=True)

        st.markdown("<div style='text-align: center;'><span style='color: #000000; font-size:1.5rem; font-weight:bold'>Tests</span></div>", unsafe_allow_html=True)

        st.markdown("<div style='text-align: center;'><span style='color: #681a49; font-size:1.5rem; font-weight:bold'>247</span></div>", unsafe_allow_html=True)

        st.markdown("<div style='text-align: center;'><span style='color: #000000; font-size:1.5rem; font-weight:bold'>% Positive</span></div>", unsafe_allow_html=True)

        st.markdown("<div style='text-align: center;'><span style='color: #681a49; font-size:1.5rem; font-weight:bold'>2.83%</span></div>", unsafe_allow_html=True)

    with columns[1]:

        bar_chart = alt.Chart(osu_data).mark_bar().encode(
            x = alt.X('date:T'),
            y = alt.Y('case:Q'),
            tooltip = ['date', 'case']
        ).properties(
            title = 'Daily cases in Ohio State'
        ).interactive(
            bind_y = False
        )

        line = alt.Chart(osu_data).mark_rule(color='#ac2217').encode(
            y='mean(case):Q',
            size=alt.SizeValue(3),
            tooltip = ['mean(case)']
        )

        chart = bar_chart + line

        st.altair_chart(chart, use_container_width = True)

    with columns[2]:

        st.markdown("<div style='background:#e6e6e6; text-align: center;'><span style='color: #ac2217; font-weight:bold'>Vaccination Rate: " +
                    vacci_rate+"</span></div>", unsafe_allow_html=True)

        donut_chart = alt.Chart(vacci_data).mark_arc(innerRadius = 70).encode(
            theta = alt.Theta(field="value", type = "quantitative"),
            color = alt.Color(field="category", type="nominal", legend=alt.Legend(orient='top', direction='vertical')),
            tooltip = ['category','value']
        ).configure_view(
            strokeWidth = 0
        )

        st.altair_chart(donut_chart, use_container_width = True)
