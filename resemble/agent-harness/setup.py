from setuptools import setup
setup(
    name='cli-anything-resemble',
    version='1.0.0',
    packages=['cli_anything.resemble'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-resemble=cli_anything.resemble:cli']},
)
