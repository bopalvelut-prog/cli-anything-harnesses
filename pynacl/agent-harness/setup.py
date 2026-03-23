from setuptools import setup
setup(
    name='cli-anything-pynacl',
    version='1.0.0',
    packages=['cli_anything.pynacl'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pynacl=cli_anything.pynacl:cli']},
)
