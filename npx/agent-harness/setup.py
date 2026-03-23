from setuptools import setup
setup(
    name='cli-anything-npx',
    version='1.0.0',
    packages=['cli_anything.npx'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-npx=cli_anything.npx:cli']},
)
