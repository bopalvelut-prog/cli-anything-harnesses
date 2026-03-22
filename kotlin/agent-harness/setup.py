from setuptools import setup
setup(
    name='cli-anything-kotlin',
    version='1.0.0',
    packages=['cli_anything.kotlin'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kotlin=cli_anything.kotlin:cli']},
)
