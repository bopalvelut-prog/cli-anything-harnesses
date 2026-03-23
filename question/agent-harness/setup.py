from setuptools import setup
setup(
    name='cli-anything-question',
    version='1.0.0',
    packages=['cli_anything.question'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-question=cli_anything.question:cli']},
)
