from setuptools import setup
setup(
    name='cli-anything-wasabi',
    version='1.0.0',
    packages=['cli_anything.wasabi'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wasabi=cli_anything.wasabi:cli']},
)
