from setuptools import setup
setup(
    name='cli-anything-app_2039',
    version='1.0.0',
    packages=['cli_anything.app_2039'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-app_2039=cli_anything.app_2039:cli']},
)
