from setuptools import setup
setup(
    name='cli-anything-knife',
    version='1.0.0',
    packages=['cli_anything.knife'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-knife=cli_anything.knife:cli']},
)
