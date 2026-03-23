from setuptools import setup
setup(
    name='cli-anything-scholar',
    version='1.0.0',
    packages=['cli_anything.scholar'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-scholar=cli_anything.scholar:cli']},
)
