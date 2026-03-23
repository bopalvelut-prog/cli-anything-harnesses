from setuptools import setup
setup(
    name='cli-anything-unlock',
    version='1.0.0',
    packages=['cli_anything.unlock'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-unlock=cli_anything.unlock:cli']},
)
