import streamlit as st
from backend.modules.css import load_css

# Load custom CSS
st.markdown(load_css(r'frontend/styles.css'), unsafe_allow_html=True)

st.title("What is Snap Scrib?")
st.write("Snap Scrib is a...")
st.subheader("Our Team:")
st.markdown(
    """
    <p align="center">
        <a href="https://github.com/cipher-shad0w" target="_blank">Cipher Shadow</a>
        <a href="https://github.com/arvedb" target="_blank">Arved Bahde</a>
        <a href="https://github.com/mirixy" target="_blank">Miriam</a>
    </p>
    """, unsafe_allow_html=True
)
st.divider()
st.markdown("""

# Snap Scrib
...

## Where to play?
[Snap Scrib](https://SnapScrib.streamlit.app)


## Demo

Coming soon

## Contributors

- [mirixy](https://github.com/mirixy)
- [cipher-shad0w](https://github.com/cipher-shad0w)
- [arvedb](https://github.com/arvedb)

## Features

- User-friendly UI.


## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/arvedb/SnapScrib.git
   cd Snap Scrib
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

3. **Enter a URL.**

## Project Structure

- `app.py`: Main file to run the Streamlit app.
- `requirements.txt`: List of Python dependencies.

## Technologies Used

- [Streamlit](https://streamlit.io/): Framework for creating interactive web applications.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.


---

If you have any questions or need further assistance, please feel free to contact any of the contributors.

Happy coding!""")