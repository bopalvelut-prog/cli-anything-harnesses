from setuptools import setup
setup(
    name='cli-anything-feedback',
    version='1.0.0',
    packages=['cli_anything.feedback'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-feedback=cli_anything.feedback:cli']},
)
