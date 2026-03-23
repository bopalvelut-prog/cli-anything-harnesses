from setuptools import setup
setup(
    name='cli-anything-jsdelivr',
    version='1.0.0',
    packages=['cli_anything.jsdelivr'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jsdelivr=cli_anything.jsdelivr:cli']},
)
