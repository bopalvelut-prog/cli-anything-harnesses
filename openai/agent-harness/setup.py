from setuptools import setup
setup(
    name='cli-anything-openai',
    version='1.0.0',
    packages=['cli_anything.openai'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-openai=cli_anything.openai:cli']},
)
