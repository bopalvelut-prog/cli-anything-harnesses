from setuptools import setup
setup(
    name='cli-anything-semantic',
    version='1.0.0',
    packages=['cli_anything.semantic'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-semantic=cli_anything.semantic:cli']},
)
