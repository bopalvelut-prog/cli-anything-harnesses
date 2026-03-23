from setuptools import setup
setup(
    name='cli-anything-strip',
    version='1.0.0',
    packages=['cli_anything.strip'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-strip=cli_anything.strip:cli']},
)
