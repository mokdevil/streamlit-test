import streamlit as st
import random

def generate_colors():
    groups = ["puisto", "hirviöt", "jannet", "siirtyvät"]
    colors = ["yellow", "orange", "red", "green", "blue", "indigo", "brown", "pink"]

    # Shuffle the colors to ensure random assignment to groups
    random.shuffle(colors)

    # Generate colors for each group without duplicates
    group_colors = []
    for i, group in enumerate(groups):
        color1 = colors[i % len(colors)]
        color2 = colors[(i + 1) % len(colors)]
        group_colors.append((group, color1, color2))

        # Remove used colors from the list
        colors.remove(color1)
        colors.remove(color2)

    return group_colors

def main():
    st.title("Random Color Generator")
    st.write("Generate two random colors for four groups of people.")

    if st.button("Generate Colors"):
        colors = generate_colors()
        for group, color1, color2 in colors:
            st.subheader(f"{group}")
            st.markdown(f"Color 1: <span style='background-color: {color1}; padding: 0.5rem'></span>", unsafe_allow_html=True)
            st.markdown(f"Color 2: <span style='background-color: {color2}; padding: 0.5rem'></span>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()