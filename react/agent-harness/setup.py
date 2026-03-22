from setuptools import setup
setup(
    name='cli-anything-react',
    version='1.0.0',
    packages=['cli_anything.react'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-react=cli_anything.react:cli']},
)
