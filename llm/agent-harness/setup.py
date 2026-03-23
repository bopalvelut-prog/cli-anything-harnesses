from setuptools import setup
setup(
    name='cli-anything-llm',
    version='1.0.0',
    packages=['cli_anything.llm'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-llm=cli_anything.llm:cli']},
)
