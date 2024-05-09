import streamlit as st
import streamlit.components.v1 as components 
from streamlit_option_menu import option_menu


html_usr="<div class='tableauPlaceholder' id='viz1715264644152' style='position: relative'><noscript><a href='#'><img alt='Dashboard 2 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Do&#47;DocBookUserDashboard&#47;Dashboard2&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='DocBookUserDashboard&#47;Dashboard2' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Do&#47;DocBookUserDashboard&#47;Dashboard2&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-GB' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1715264644152');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='800px';vizElement.style.height='627px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='800px';vizElement.style.height='627px';} else { vizElement.style.width='100%';vizElement.style.height='1327px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"
html_doc="<div class='tableauPlaceholder' id='viz1715264824197' style='position: relative'><noscript><a href='#'><img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Do&#47;DocBookUserDashboard&#47;Dashboard1&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='DocBookUserDashboard&#47;Dashboard1' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Do&#47;DocBookUserDashboard&#47;Dashboard1&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-GB' /><param name='filter' value='publish=yes' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1715264824197');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='800px';vizElement.style.height='627px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='800px';vizElement.style.height='627px';} else { vizElement.style.width='100%';vizElement.style.height='1327px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"


with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home",
            "User Statistics",
            "Doctor Statistics",            
        ],
        default_index=0,
    )

st.title("DocBook: The Doctor Availability Portal")


header = st.container()
user=st.container()
doc=st.container()
if selected=="Home":
    with header:
        st.write("""Our project's core goal is to develop a user-friendly dashboard and appointment system that
        simplifies the process of checking and connecting with available doctors, particularlyduringbusy festive periods. We aim to enhance the overall healthcare experience for patients byproviding an intuitive interface that allows quick access to doctor availability. The appointment
        system will streamline the booking process, ensuring a seamless connection between patients andhealthcare providers. Our user-centric approach recognizes the challenges of festive times, prioritizing easy access to medical assistance. In summary, our project aims to create an efficient
        and accessible healthcare system, contributing to a positive experience for both patients andhealthcare providers.""")
        st.divider()
        st.image("architechture.png", caption="DocBook Architechture")
        st.divider()
if selected=="User Statistics":
    st.header("User Activity Dashboard: Transparent Appointment Management")
    st.write(""" This is a dashboard of User Demographics Filled as per DocBook's Portal""")
    components.html(html_usr, width=800, height=600,scrolling=False)

if selected=="Doctor Statistics":
    st.header("User Activity Dashboard: Showcasing our Doctor Network")
    st.write(""" This is a dashboard of Doctor Demographics Filled as per DocBook's Portal""")
    components.html(html_doc, width=800, height=600,scrolling=False)