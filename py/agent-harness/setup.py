from setuptools import setup
setup(
    name='cli-anything-py',
    version='1.0.0',
    packages=['cli_anything.py'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-py=cli_anything.py:cli']},
)
