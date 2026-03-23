from setuptools import setup
setup(
    name='cli-anything-job',
    version='1.0.0',
    packages=['cli_anything.job'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-job=cli_anything.job:cli']},
)
