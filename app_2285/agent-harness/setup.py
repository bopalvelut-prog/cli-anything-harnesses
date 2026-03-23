from setuptools import setup
setup(
    name='cli-anything-app_2285',
    version='1.0.0',
    packages=['cli_anything.app_2285'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-app_2285=cli_anything.app_2285:cli']},
)
