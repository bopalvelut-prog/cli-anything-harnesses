from setuptools import setup
setup(
    name='cli-anything-might',
    version='1.0.0',
    packages=['cli_anything.might'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-might=cli_anything.might:cli']},
)
