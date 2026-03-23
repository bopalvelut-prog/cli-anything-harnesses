from setuptools import setup
setup(
    name='cli-anything-dark',
    version='1.0.0',
    packages=['cli_anything.dark'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-dark=cli_anything.dark:cli']},
)
