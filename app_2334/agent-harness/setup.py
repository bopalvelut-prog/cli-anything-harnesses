from setuptools import setup
setup(
    name='cli-anything-app_2334',
    version='1.0.0',
    packages=['cli_anything.app_2334'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-app_2334=cli_anything.app_2334:cli']},
)
