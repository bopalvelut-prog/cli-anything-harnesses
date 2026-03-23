from setuptools import setup
setup(
    name='cli-anything-establish',
    version='1.0.0',
    packages=['cli_anything.establish'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-establish=cli_anything.establish:cli']},
)
