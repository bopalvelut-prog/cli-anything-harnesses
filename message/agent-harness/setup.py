from setuptools import setup
setup(
    name='cli-anything-message',
    version='1.0.0',
    packages=['cli_anything.message'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-message=cli_anything.message:cli']},
)
