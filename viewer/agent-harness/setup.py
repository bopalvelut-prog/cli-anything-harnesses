from setuptools import setup
setup(
    name='cli-anything-viewer',
    version='1.0.0',
    packages=['cli_anything.viewer'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-viewer=cli_anything.viewer:cli']},
)
