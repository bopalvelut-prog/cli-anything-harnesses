from setuptools import setup
setup(
    name='cli-anything-sublime',
    version='1.0.0',
    packages=['cli_anything.sublime'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-sublime=cli_anything.sublime:cli']},
)
