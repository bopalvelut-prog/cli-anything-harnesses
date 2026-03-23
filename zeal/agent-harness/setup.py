from setuptools import setup
setup(
    name='cli-anything-zeal',
    version='1.0.0',
    packages=['cli_anything.zeal'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-zeal=cli_anything.zeal:cli']},
)
