from setuptools import setup
setup(
    name='cli-anything-codewhisperer',
    version='1.0.0',
    packages=['cli_anything.codewhisperer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-codewhisperer=cli_anything.codewhisperer:cli']},
)
