from setuptools import setup
setup(
    name='cli-anything-wget',
    version='1.0.0',
    packages=['cli_anything.wget'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-wget=cli_anything.wget:cli']},
)
