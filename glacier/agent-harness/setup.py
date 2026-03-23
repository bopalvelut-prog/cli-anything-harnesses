from setuptools import setup
setup(
    name='cli-anything-glacier',
    version='1.0.0',
    packages=['cli_anything.glacier'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-glacier=cli_anything.glacier:cli']},
)
