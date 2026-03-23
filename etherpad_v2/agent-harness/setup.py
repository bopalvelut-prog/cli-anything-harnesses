from setuptools import setup
setup(
    name='cli-anything-etherpad_v2',
    version='1.0.0',
    packages=['cli_anything.etherpad_v2'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-etherpad_v2=cli_anything.etherpad_v2:cli']},
)
