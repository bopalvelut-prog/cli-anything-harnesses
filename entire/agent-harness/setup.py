from setuptools import setup
setup(
    name='cli-anything-entire',
    version='1.0.0',
    packages=['cli_anything.entire'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-entire=cli_anything.entire:cli']},
)
