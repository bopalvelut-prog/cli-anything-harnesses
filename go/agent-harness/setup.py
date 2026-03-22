from setuptools import setup
setup(
    name='cli-anything-go',
    version='1.0.0',
    packages=['cli_anything.go'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-go=cli_anything.go:cli']},
)
