from setuptools import setup
setup(
    name='cli-anything-app_5853',
    version='1.0.0',
    packages=['cli_anything.app_5853'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-app_5853=cli_anything.app_5853:cli']},
)
