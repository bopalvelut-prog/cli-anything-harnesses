from setuptools import setup
setup(
    name='cli-anything-polaris',
    version='1.0.0',
    packages=['cli_anything.polaris'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-polaris=cli_anything.polaris:cli']},
)
