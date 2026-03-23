from setuptools import setup
setup(
    name='cli-anything-text',
    version='1.0.0',
    packages=['cli_anything.text'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-text=cli_anything.text:cli']},
)
