from setuptools import setup
setup(
    name='cli-anything-zappa',
    version='1.0.0',
    packages=['cli_anything.zappa'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-zappa=cli_anything.zappa:cli']},
)
