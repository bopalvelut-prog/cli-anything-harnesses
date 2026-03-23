from setuptools import setup
setup(
    name='cli-anything-colonel',
    version='1.0.0',
    packages=['cli_anything.colonel'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-colonel=cli_anything.colonel:cli']},
)
