from setuptools import setup
setup(
    name='cli-anything-latter',
    version='1.0.0',
    packages=['cli_anything.latter'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-latter=cli_anything.latter:cli']},
)
