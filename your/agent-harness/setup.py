from setuptools import setup
setup(
    name='cli-anything-your',
    version='1.0.0',
    packages=['cli_anything.your'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-your=cli_anything.your:cli']},
)
