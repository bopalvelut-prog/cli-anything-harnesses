from setuptools import setup
setup(
    name='cli-anything-slow',
    version='1.0.0',
    packages=['cli_anything.slow'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-slow=cli_anything.slow:cli']},
)
