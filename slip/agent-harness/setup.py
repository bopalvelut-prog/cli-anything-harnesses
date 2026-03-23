from setuptools import setup
setup(
    name='cli-anything-slip',
    version='1.0.0',
    packages=['cli_anything.slip'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-slip=cli_anything.slip:cli']},
)
