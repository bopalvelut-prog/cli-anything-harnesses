from setuptools import setup
setup(
    name='cli-anything-vite',
    version='1.0.0',
    packages=['cli_anything.vite'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vite=cli_anything.vite:cli']},
)
