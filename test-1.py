import streamlit as st

def intro():
    import streamlit as st

    st.write("# Welcome to Streamlit! 👋")
    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        Streamlit is an open-source app framework built specifically for
        Machine Learning and Data Science projects.

        **👈 Select a demo from the dropdown on the left** to see some examples
        of what Streamlit can do!

        ### Want to learn more?

        - Check out [streamlit.io](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
        - Ask a question in our [community
          forums](https://discuss.streamlit.io)

        ### See more complex demos

        - Use a neural net to [analyze the Udacity Self-driving Car Image
          Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )

def mapping_demo():
    import streamlit as st
    import pandas as pd
    import pydeck as pdk

    from urllib.error import URLError

    st.markdown(f"# {list(page_names_to_funcs.keys())[1]}")
    st.write(
        """
        This demo shows how to use
[`st.pydeck_chart`](https://docs.streamlit.io/library/api-reference/charts/st.pydeck_chart)
to display geospatial data.
"""
    )

    @st.cache_data
    def from_data_file(filename):
        url = (
            "http://raw.githubusercontent.com/streamlit/"
            "example-data/master/hello/v1/%s" % filename
        )
        return pd.read_json(url)

    try:
        ALL_LAYERS = {
            "Bike Rentals": pdk.Layer(
                "HexagonLayer",
                data=from_data_file("bike_rental_stats.json"),
                get_position=["lon", "lat"],
                radius=200,
                elevation_scale=4,
                elevation_range=[0, 1000],
                extruded=True,
            ),
            "Bart Stop Exits": pdk.Layer(
                "ScatterplotLayer",
                data=from_data_file("bart_stop_stats.json"),
                get_position=["lon", "lat"],
                get_color=[200, 30, 0, 160],
                get_radius="[exits]",
                radius_scale=0.05,
            ),
            "Bart Stop Names": pdk.Layer(
                "TextLayer",
                data=from_data_file("bart_stop_stats.json"),
                get_position=["lon", "lat"],
                get_text="name",
                get_color=[0, 0, 0, 200],
                get_size=15,
                get_alignment_baseline="'bottom'",
            ),
            "Outbound Flow": pdk.Layer(
                "ArcLayer",
                data=from_data_file("bart_path_stats.json"),
                get_source_position=["lon", "lat"],
                get_target_position=["lon2", "lat2"],
                get_source_color=[200, 30, 0, 160],
                get_target_color=[200, 30, 0, 160],
                auto_highlight=True,
                width_scale=0.0001,
                get_width="outbound",
                width_min_pixels=3,
                width_max_pixels=30,
            ),
        }
        st.sidebar.markdown("### Map Layers")
        selected_layers = [
            layer
            for layer_name, layer in ALL_LAYERS.items()
            if st.sidebar.checkbox(layer_name, True)
        ]
        if selected_layers:
            st.pydeck_chart(
                pdk.Deck(
                    map_style="mapbox://styles/mapbox/light-v9",
                    initial_view_state={
                        "latitude": 37.76,
                        "longitude": -122.4,
                        "zoom": 11,
                        "pitch": 50,
                    },
                    layers=selected_layers,
                )
            )
        else:
            st.error("Please choose at least one layer above.")
    except URLError as e:
        st.error(
            """
            **This demo requires internet access.**

            Connection error: %s
        """
            % e.reason
        )

def plotting_demo():

    import streamlit as st
    import time
    import numpy as np

    st.markdown(f'# {list(page_names_to_funcs.keys())[2]}')
    st.write(
        """
        This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!
"""
    )
    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()
    last_rows = np.random.randn(1, 1)
    chart = st.line_chart(last_rows)

    for i in range(1, 101):
        new_rows = last_rows[-1, :] + np.random.randn(10, 1).cumsum(axis=0)
        status_text.text("%i%% Complete" % i)
        chart.add_rows(new_rows)
        progress_bar.progress(i)
        last_rows = new_rows
        time.sleep(0.05)

    progress_bar.empty()
    
    # Streamlit widgets automatically run the script from top to bottom. Since
    # this button is not connected to any other logic, it just causes a plain
    # rerun.
    st.button("Re-run")

def animation_demo():
    from typing import Any

    import numpy as np

    import streamlit as st

    def animation() -> None:

        # Interactive Streamlit elements, like these sliders, return their value.
        # This gives you an extremely simple interaction model.
        iterations = st.sidebar.slider("Level of detail", 2, 20, 10, 1)
        separation = st.sidebar.slider("Separation", 0.7, 2.0, 0.7885)

        # Non-interactive elements return a placeholder to their location
        # in the app. Here we're storing progress_bar to update it later.
        progress_bar = st.sidebar.progress(0)

        # These two elements will be filled in later, so we create a placeholder
        # for them using st.empty()
        frame_text = st.sidebar.empty()
        image = st.empty()

        m, n, s = 960, 640, 400
        x = np.linspace(-m / s, m / s, num=m).reshape((1, m))
        y = np.linspace(-n / s, n / s, num=n).reshape((n, 1))

        for frame_num, a in enumerate(np.linspace(0.0, 4 * np.pi, 100)):
            # Here were setting value for these two elements.
            progress_bar.progress(frame_num)
            frame_text.text("Frame %i/100" % (frame_num + 1))

            # Performing some fractal wizardry.
            c = separation * np.exp(1j * a)
            Z = np.tile(x, (n, 1)) + 1j * np.tile(y, (1, m))
            C = np.full((n, m), c)
            M: Any = np.full((n, m), True, dtype=bool)
            N = np.zeros((n, m))

            for i in range(iterations):
                Z[M] = Z[M] * Z[M] + C[M]
                M[np.abs(Z) > 2] = False
                N[M] = i

            # Update the image placeholder by calling the image() function on it.
            image.image(1.0 - (N / N.max()), use_column_width=True)

        # We clear elements by calling empty on them.
        progress_bar.empty()
        frame_text.empty()

        # Streamlit widgets automatically run the script from top to bottom. Since
        # this button is not connected to any other logic, it just causes a plain
        # rerun.
        st.button("Re-run")

    st.markdown("# Animation Demo")
    st.sidebar.header("Animation Demo")
    st.write(
        """This app shows how you can use Streamlit to build cool animations.
    It displays an animated fractal based on the the Julia Set. Use the slider
    to tune different parameters."""
    )

    animation()

def uber():
    import streamlit as st
    import pandas as pd
    import numpy as np

    st.title('Uber pickups in NYC')

    DATE_COLUMN = 'date/time'
    DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
                'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

    @st.cache_data
    def load_data(nrows):
        data = pd.read_csv(DATA_URL, nrows=nrows)
        lowercase = lambda x: str(x).lower()
        data.rename(lowercase, axis='columns', inplace=True)
        data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
        return data

    data_load_state = st.text('Loading data...')
    data = load_data(10000)
    data_load_state.text("Done! (using st.cache_data)")

    if st.checkbox('Show raw data'):
        st.subheader('Raw data')
        st.write(data)

    with st.expander("Number of pickups per hour charts"):
        hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
        st.bar_chart(hist_values)
        line_chart = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
        st.line_chart(line_chart)
        area_chart = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
        st.area_chart(area_chart)

    # Some number in the range 0-23
    hour_to_filter = st.slider('hour', 0, 23, 17)
    filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

    st.subheader('Map of all pickups at %s:00' % hour_to_filter)
    st.map(filtered_data)

def yt_thumbnail():
    import streamlit as st

    st.title('🖼️ yt-img-app')
    st.header('YouTube Thumbnail Image Extractor App')

    #with st.expander('About this app'):
    st.write('This app retrieves the thumbnail image from a YouTube video.')

    # Image settings
    st.sidebar.header('Settings')
    img_dict = {'Max': 'maxresdefault', 'High': 'hqdefault', 'Medium': 'mqdefault', 'Standard': 'sddefault'}
    selected_img_quality = st.sidebar.selectbox('Select image quality', ['Max', 'High', 'Medium', 'Standard'])
    img_quality = img_dict[selected_img_quality]

    yt_url = st.text_input('Paste YouTube URL', 'https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    def get_ytid(input_url):
        if 'youtu.be' in input_url:
            ytid = input_url.split('/')[-1]
        if 'youtube.com' in input_url:
            ytid = input_url.split('=')[-1]
        return ytid

    # Display YouTube thumbnail image
    if yt_url != '':
        ytid = get_ytid(yt_url) # yt or yt_url

        yt_img = f'http://img.youtube.com/vi/{ytid}/{img_quality}.jpg'
        st.image(yt_img)
        st.write('YouTube video thumbnail image URL: ', yt_img)
    else:
        st.write('☝️ Enter URL to continue ...')
    
def calculator():
    import streamlit as st

    st.title("Simple calculator")

    # This function adds two numbers
    def add(x, y):
        return x + y

    # This function subtracts two numbers
    def subtract(x, y):
        return x - y

    # This function multiplies two numbers
    def multiply(x, y):
        return x * y

    # This function divides two numbers
    def divide(x, y):
        return x / y

    # take input from the user
    choice = st.radio("Select an operation", ("Add", "Subtract", "Multiply", "Divide"), horizontal=True)

    # check if choice is one of the four options
    num1 = st.number_input("Enter first number: ")
    num2 = st.number_input("Enter second number: ")
    if choice == 'Add':
        st.write(num1, "+", num2, "=", add(num1, num2))

    elif choice == 'Subtract':
        st.write(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == 'Multiply':
        st.write(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == 'Divide':
        st.write(num1, "/", num2, "=", divide(num1, num2))

def file_uploader():
    import streamlit as st
    import pandas as pd
    from PIL import Image

    st.title("File uploader test")
    st.write("Choose a .py, .jpeg or a .txt file")

    uploaded_file = st.file_uploader("Choose a file", type=["py", "jpeg", "txt", "csv"])

    def read_python():
        with uploaded_file as f:
                code_string = read_file(f)
                start_index = code_string.find('st.set_page_config(')
                end_index = code_string.find(')', start_index)
                new_code_string = code_string[:start_index] + code_string[end_index+1:]
                if st.checkbox("Show source code", False):
                    st.code(code_string, language=("python"))
                if st.checkbox("Run python script", False):
                    exec(new_code_string)

    def read_text():
        with uploaded_file as f:
                op = st.selectbox(
                    'Select how to display text',
                    ("Text", "Code", "Write"))
                if op == "Text":
                    st.text(read_file(f))
                elif op == "Code":
                    st.code(read_file(f))
                elif op == "Write":
                    st.write(read_file(f))
    
    def read_image():
        Image.open(uploaded_file)
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    def read_csv():
        data = pd.read_csv(uploaded_file)
        st.dataframe(data)

    def read_file(file):
        return file.read().decode("utf-8")

    if uploaded_file is not None:
        filename = uploaded_file.name

        if filename.endswith(".py"):
            read_python()
        elif filename.endswith(".txt"):
            read_text()
        elif filename.endswith(".jpeg"):
            read_image()
        elif filename.endswith(".csv"):
            read_csv()

def test():
    text = st.text_area("Test: ", value= "Text")
    st.download_button("Download file", data=text, file_name="test.txt")

page_names_to_funcs = {
    "—": intro,
    "Mapping Demo": mapping_demo,
    "Plotting Demo": plotting_demo,
    "Animation Demo": animation_demo,
    "Uber pickups": uber,
    "Youtube Thumbnail": yt_thumbnail,
    "Simple calculator": calculator,
    "File uploader test": file_uploader,
    "Test": test
}

demo_name = st.sidebar.selectbox("Choose a demo", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
