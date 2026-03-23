from setuptools import setup
setup(
    name='cli-anything-driver',
    version='1.0.0',
    packages=['cli_anything.driver'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-driver=cli_anything.driver:cli']},
)
