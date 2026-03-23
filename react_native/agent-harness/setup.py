from setuptools import setup
setup(
    name='cli-anything-react_native',
    version='1.0.0',
    packages=['cli_anything.react_native'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-react_native=cli_anything.react_native:cli']},
)
