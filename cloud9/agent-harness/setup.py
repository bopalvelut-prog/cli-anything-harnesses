from setuptools import setup
setup(
    name='cli-anything-cloud9',
    version='1.0.0',
    packages=['cli_anything.cloud9'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cloud9=cli_anything.cloud9:cli']},
)
