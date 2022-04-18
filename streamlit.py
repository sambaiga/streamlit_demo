import streamlit as st
import hydralit_components as hc
import pandas as pd
import altair as alt
import plotly.express as px

st.set_page_config(layout='wide',initial_sidebar_state='collapsed',)
@st.cache(allow_output_mutation=True)
def load_data():
    data = pd.read_csv('swiss_power_demand.csv')
    return data








menu_data = [
    {'icon':"far fa-line-chart", 'label':"Data Analysis"},
    {'icon':"far fa-info-circle", 'label':"Forecasting"}, 
]


over_theme = {'txc_inactive': '#FFFFFF'}
menu_id = hc.nav_bar(
    menu_definition=menu_data,
    override_theme=over_theme,
    home_name='Home',
    #login_name='Logout',
    hide_streamlit_markers=False, #will show the st hamburger as well as the navbar now!
    sticky_nav=True, #at the top or not
    sticky_mode='pinned', #jumpy or not-jumpy, but sticky or pinned
)




def main():
    #get the id of the menu item clicked
   
    if f"{menu_id}"=="Home":
        row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns(
            (.1, 3, .2, 0.5, .1))

        row0_1.title('FPSe2Q Power Demand Forecasting Demo')

        with row0_2:
            st.write('')

        
        row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns(
            (.1, 3, 0.1, 4,  .1))
        row0_1.image('FPQ_arch.png', use_column_width=True)

        container = row0_2.container()
        container.write("The increased penetration of RES as part of a decentralized and distributed power system makes load forecasting a critical component in the planning and operation of power systems. However, producing accurate short-term load forecasts at the distribution level is complex compared to the transmission level. Moreover, owing to the stochastic nature of RES, it is necessary to quantify the uncertainty of the forecasted load at any given time, which is critical for the real-world decision process.")
        container.markdown("The FPSe2Q  model the conditional distribution $$p(\mathbf{y}_{i,t+1:T}|\mathbf{x}_{i,t:t-L}, \mathbf{z}_{i,t+1:T})$$ ")


    if f"{menu_id}"=="Data Analysis":
        data = load_data()
        fig = px.scatter(data, x="timestamp", y="Load", color="Season")
        st.plotly_chart(fig, use_container_width=True)
        alt.themes.enable("opaque")
        chart = (
            alt.Chart(data.reset_index())
            .mark_circle(size=20)
            .encode(x = alt.X('timestamp:T', title=''), 
                    y = alt.Y('Load:Q', title='Aggregated Demands (KW)'),
                    color=alt.Color('Season', scale=alt.Scale(scheme='tableau10'))))



        
        chart.configure_axis(
            grid=False,
        ).configure_view(
            strokeOpacity=0
        )
        # Display both charts together
        st.altair_chart(chart.interactive(), use_container_width=True)


main()