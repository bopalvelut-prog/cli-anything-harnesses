from setuptools import setup
setup(
    name='cli-anything-gcp_dialogflow',
    version='1.0.0',
    packages=['cli_anything.gcp_dialogflow'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gcp_dialogflow=cli_anything.gcp_dialogflow:cli']},
)
