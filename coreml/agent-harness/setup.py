from setuptools import setup
setup(
    name='cli-anything-coreml',
    version='1.0.0',
    packages=['cli_anything.coreml'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-coreml=cli_anything.coreml:cli']},
)
