from setuptools import setup
setup(
    name='cli-anything-judge',
    version='1.0.0',
    packages=['cli_anything.judge'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-judge=cli_anything.judge:cli']},
)
