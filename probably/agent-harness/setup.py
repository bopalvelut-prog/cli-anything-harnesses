from setuptools import setup
setup(
    name='cli-anything-probably',
    version='1.0.0',
    packages=['cli_anything.probably'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-probably=cli_anything.probably:cli']},
)
