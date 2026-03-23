from setuptools import setup
setup(
    name='cli-anything-aroma',
    version='1.0.0',
    packages=['cli_anything.aroma'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-aroma=cli_anything.aroma:cli']},
)
