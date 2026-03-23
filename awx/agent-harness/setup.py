from setuptools import setup
setup(
    name='cli-anything-awx',
    version='1.0.0',
    packages=['cli_anything.awx'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-awx=cli_anything.awx:cli']},
)
