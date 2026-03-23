from setuptools import setup
setup(
    name='cli-anything-track',
    version='1.0.0',
    packages=['cli_anything.track'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-track=cli_anything.track:cli']},
)
