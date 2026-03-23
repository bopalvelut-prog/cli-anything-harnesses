from setuptools import setup
setup(
    name='cli-anything-ollama2',
    version='1.0.0',
    packages=['cli_anything.ollama2'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ollama2=cli_anything.ollama2:cli']},
)
