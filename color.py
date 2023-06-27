import streamlit as st
import random

def generate_colors():
    groups = ["puisto", "hirviöt", "siirtyvät", "jannet"]
    colors = [
        ("Yellow", "#FFFF00"),
        ("Orange", "#FFA500"),
        ("Red", "#FF0000"),
        ("Green", "#008000"),
        ("Blue", "#0000FF"),
        ("Indigo", "#4B0082"),
        ("Brown", "#964B00"),
        ("Pink", "#FFC0CB")
    ]

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
    st.title("Kesäjuhliin väri valija")
    st.write("painat nappia ohjelma generoi neljälle ryhmälle kahdet värit.")

    if st.button("Generate Colors"):
        colors = generate_colors()
        for group, (color1_name, color1_hex), (color2_name, color2_hex) in colors:
            st.subheader(f"{group}")
            st.markdown(f"Color 1: <span style='background-color: {color1_hex}; padding: 0.5rem'></span> {color1_name}", unsafe_allow_html=True)
            st.markdown(f"Color 2: <span style='background-color: {color2_hex}; padding: 0.5rem'></span> {color2_name}", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
