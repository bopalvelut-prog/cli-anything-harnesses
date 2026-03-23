from setuptools import setup
setup(
    name='cli-anything-app_5754',
    version='1.0.0',
    packages=['cli_anything.app_5754'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-app_5754=cli_anything.app_5754:cli']},
)
