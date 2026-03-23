from setuptools import setup
setup(
    name='cli-anything-framer',
    version='1.0.0',
    packages=['cli_anything.framer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-framer=cli_anything.framer:cli']},
)
