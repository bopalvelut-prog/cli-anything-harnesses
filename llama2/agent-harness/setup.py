from setuptools import setup
setup(
    name='cli-anything-llama2',
    version='1.0.0',
    packages=['cli_anything.llama2'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-llama2=cli_anything.llama2:cli']},
)
