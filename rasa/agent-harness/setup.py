from setuptools import setup
setup(
    name='cli-anything-rasa',
    version='1.0.0',
    packages=['cli_anything.rasa'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-rasa=cli_anything.rasa:cli']},
)
