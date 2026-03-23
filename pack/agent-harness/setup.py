from setuptools import setup
setup(
    name='cli-anything-pack',
    version='1.0.0',
    packages=['cli_anything.pack'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-pack=cli_anything.pack:cli']},
)
