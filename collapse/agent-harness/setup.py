from setuptools import setup
setup(
    name='cli-anything-collapse',
    version='1.0.0',
    packages=['cli_anything.collapse'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-collapse=cli_anything.collapse:cli']},
)
