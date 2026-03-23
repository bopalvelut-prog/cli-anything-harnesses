from setuptools import setup
setup(
    name='cli-anything-breast',
    version='1.0.0',
    packages=['cli_anything.breast'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-breast=cli_anything.breast:cli']},
)
