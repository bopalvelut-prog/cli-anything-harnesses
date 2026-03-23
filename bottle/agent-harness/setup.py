from setuptools import setup
setup(
    name='cli-anything-bottle',
    version='1.0.0',
    packages=['cli_anything.bottle'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-bottle=cli_anything.bottle:cli']},
)
