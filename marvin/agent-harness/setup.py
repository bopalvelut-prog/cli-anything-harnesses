from setuptools import setup
setup(
    name='cli-anything-marvin',
    version='1.0.0',
    packages=['cli_anything.marvin'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-marvin=cli_anything.marvin:cli']},
)
