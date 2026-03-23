from setuptools import setup
setup(
    name='cli-anything-indeed',
    version='1.0.0',
    packages=['cli_anything.indeed'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-indeed=cli_anything.indeed:cli']},
)
