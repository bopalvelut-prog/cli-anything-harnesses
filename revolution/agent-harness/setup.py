from setuptools import setup
setup(
    name='cli-anything-revolution',
    version='1.0.0',
    packages=['cli_anything.revolution'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-revolution=cli_anything.revolution:cli']},
)
