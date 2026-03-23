from setuptools import setup
setup(
    name='cli-anything-streamlit',
    version='1.0.0',
    packages=['cli_anything.streamlit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-streamlit=cli_anything.streamlit:cli']},
)
