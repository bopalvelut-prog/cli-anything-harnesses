from setuptools import setup
setup(
    name='cli-anything-after',
    version='1.0.0',
    packages=['cli_anything.after'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-after=cli_anything.after:cli']},
)
