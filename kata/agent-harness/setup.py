from setuptools import setup
setup(
    name='cli-anything-kata',
    version='1.0.0',
    packages=['cli_anything.kata'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-kata=cli_anything.kata:cli']},
)
