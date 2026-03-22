from setuptools import setup
setup(
    name='cli-anything-app_525',
    version='1.0.0',
    packages=['cli_anything.app_525'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-app_525=cli_anything.app_525:cli']},
)
