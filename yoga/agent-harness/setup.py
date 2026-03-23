from setuptools import setup
setup(
    name='cli-anything-yoga',
    version='1.0.0',
    packages=['cli_anything.yoga'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-yoga=cli_anything.yoga:cli']},
)
