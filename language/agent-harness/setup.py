from setuptools import setup
setup(
    name='cli-anything-language',
    version='1.0.0',
    packages=['cli_anything.language'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-language=cli_anything.language:cli']},
)
