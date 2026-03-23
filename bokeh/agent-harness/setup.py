from setuptools import setup
setup(
    name='cli-anything-bokeh',
    version='1.0.0',
    packages=['cli_anything.bokeh'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bokeh=cli_anything.bokeh:cli']},
)
