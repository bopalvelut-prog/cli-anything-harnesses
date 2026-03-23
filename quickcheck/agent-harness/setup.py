from setuptools import setup
setup(
    name='cli-anything-quickcheck',
    version='1.0.0',
    packages=['cli_anything.quickcheck'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-quickcheck=cli_anything.quickcheck:cli']},
)
