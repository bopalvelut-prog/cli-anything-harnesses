from setuptools import setup
setup(
    name='cli-anything-dinner',
    version='1.0.0',
    packages=['cli_anything.dinner'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dinner=cli_anything.dinner:cli']},
)
