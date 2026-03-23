from setuptools import setup
setup(
    name='cli-anything-codesandbox',
    version='1.0.0',
    packages=['cli_anything.codesandbox'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-codesandbox=cli_anything.codesandbox:cli']},
)
