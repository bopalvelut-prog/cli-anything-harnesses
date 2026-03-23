from setuptools import setup
setup(
    name='cli-anything-recruit',
    version='1.0.0',
    packages=['cli_anything.recruit'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-recruit=cli_anything.recruit:cli']},
)
