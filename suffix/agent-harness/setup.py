from setuptools import setup
setup(
    name='cli-anything-suffix',
    version='1.0.0',
    packages=['cli_anything.suffix'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-suffix=cli_anything.suffix:cli']},
)
