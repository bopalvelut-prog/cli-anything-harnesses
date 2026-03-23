from setuptools import setup
setup(
    name='cli-anything-visual',
    version='1.0.0',
    packages=['cli_anything.visual'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-visual=cli_anything.visual:cli']},
)
