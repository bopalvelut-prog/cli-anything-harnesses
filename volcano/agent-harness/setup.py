from setuptools import setup
setup(
    name='cli-anything-volcano',
    version='1.0.0',
    packages=['cli_anything.volcano'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-volcano=cli_anything.volcano:cli']},
)
