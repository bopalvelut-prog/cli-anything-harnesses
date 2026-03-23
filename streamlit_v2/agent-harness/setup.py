from setuptools import setup
setup(
    name='cli-anything-streamlit_v2',
    version='1.0.0',
    packages=['cli_anything.streamlit_v2'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-streamlit_v2=cli_anything.streamlit_v2:cli']},
)
