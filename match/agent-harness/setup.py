from setuptools import setup
setup(
    name='cli-anything-match',
    version='1.0.0',
    packages=['cli_anything.match'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-match=cli_anything.match:cli']},
)
