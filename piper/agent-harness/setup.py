from setuptools import setup
setup(
    name='cli-anything-piper',
    version='1.0.0',
    packages=['cli_anything.piper'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-piper=cli_anything.piper:cli']},
)
