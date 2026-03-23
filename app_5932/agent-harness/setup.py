from setuptools import setup
setup(
    name='cli-anything-app_5932',
    version='1.0.0',
    packages=['cli_anything.app_5932'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-app_5932=cli_anything.app_5932:cli']},
)
