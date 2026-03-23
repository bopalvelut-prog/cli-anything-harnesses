from setuptools import setup
setup(
    name='cli-anything-async',
    version='1.0.0',
    packages=['cli_anything.async'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-async=cli_anything.async:cli']},
)
