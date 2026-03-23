from setuptools import setup
setup(
    name='cli-anything-emit',
    version='1.0.0',
    packages=['cli_anything.emit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-emit=cli_anything.emit:cli']},
)
