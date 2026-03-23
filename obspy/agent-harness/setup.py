from setuptools import setup
setup(
    name='cli-anything-obspy',
    version='1.0.0',
    packages=['cli_anything.obspy'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-obspy=cli_anything.obspy:cli']},
)
