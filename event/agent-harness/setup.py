from setuptools import setup
setup(
    name='cli-anything-event',
    version='1.0.0',
    packages=['cli_anything.event'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-event=cli_anything.event:cli']},
)
