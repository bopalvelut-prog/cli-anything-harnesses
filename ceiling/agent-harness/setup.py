from setuptools import setup
setup(
    name='cli-anything-ceiling',
    version='1.0.0',
    packages=['cli_anything.ceiling'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ceiling=cli_anything.ceiling:cli']},
)
