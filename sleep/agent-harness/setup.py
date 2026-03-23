from setuptools import setup
setup(
    name='cli-anything-sleep',
    version='1.0.0',
    packages=['cli_anything.sleep'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sleep=cli_anything.sleep:cli']},
)
