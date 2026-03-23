from setuptools import setup
setup(
    name='cli-anything-come',
    version='1.0.0',
    packages=['cli_anything.come'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-come=cli_anything.come:cli']},
)
