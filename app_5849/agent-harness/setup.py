from setuptools import setup
setup(
    name='cli-anything-app_5849',
    version='1.0.0',
    packages=['cli_anything.app_5849'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-app_5849=cli_anything.app_5849:cli']},
)
