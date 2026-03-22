from setuptools import setup
setup(
    name='cli-anything-ghostscript',
    version='1.0.0',
    packages=['cli_anything.ghostscript'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-ghostscript=cli_anything.ghostscript:cli']},
)
