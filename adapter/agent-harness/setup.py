from setuptools import setup
setup(
    name='cli-anything-adapter',
    version='1.0.0',
    packages=['cli_anything.adapter'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-adapter=cli_anything.adapter:cli']},
)
