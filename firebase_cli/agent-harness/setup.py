from setuptools import setup
setup(
    name='cli-anything-firebase_cli',
    version='1.0.0',
    packages=['cli_anything.firebase_cli'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-firebase_cli=cli_anything.firebase_cli:cli']},
)
