from setuptools import setup
setup(
    name='cli-anything-word',
    version='1.0.0',
    packages=['cli_anything.word'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-word=cli_anything.word:cli']},
)
