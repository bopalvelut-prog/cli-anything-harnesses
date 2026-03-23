from setuptools import setup
setup(
    name='cli-anything-stub',
    version='1.0.0',
    packages=['cli_anything.stub'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-stub=cli_anything.stub:cli']},
)
