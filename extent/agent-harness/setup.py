from setuptools import setup
setup(
    name='cli-anything-extent',
    version='1.0.0',
    packages=['cli_anything.extent'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-extent=cli_anything.extent:cli']},
)
