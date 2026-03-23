from setuptools import setup
setup(
    name='cli-anything-jakarta',
    version='1.0.0',
    packages=['cli_anything.jakarta'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-jakarta=cli_anything.jakarta:cli']},
)
