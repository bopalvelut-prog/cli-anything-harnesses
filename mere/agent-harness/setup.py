from setuptools import setup
setup(
    name='cli-anything-mere',
    version='1.0.0',
    packages=['cli_anything.mere'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-mere=cli_anything.mere:cli']},
)
