from setuptools import setup
setup(
    name='cli-anything-plotly',
    version='1.0.0',
    packages=['cli_anything.plotly'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-plotly=cli_anything.plotly:cli']},
)
