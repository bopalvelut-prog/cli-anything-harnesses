from setuptools import setup
setup(
    name='cli-anything-arsenal',
    version='1.0.0',
    packages=['cli_anything.arsenal'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-arsenal=cli_anything.arsenal:cli']},
)
