from setuptools import setup
setup(
    name='cli-anything-gcp_speech',
    version='1.0.0',
    packages=['cli_anything.gcp_speech'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-gcp_speech=cli_anything.gcp_speech:cli']},
)
