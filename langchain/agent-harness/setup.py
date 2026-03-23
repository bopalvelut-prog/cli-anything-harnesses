from setuptools import setup
setup(
    name='cli-anything-langchain',
    version='1.0.0',
    packages=['cli_anything.langchain'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-langchain=cli_anything.langchain:cli']},
)
