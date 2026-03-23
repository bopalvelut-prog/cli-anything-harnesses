from setuptools import setup
setup(
    name='cli-anything-vision',
    version='1.0.0',
    packages=['cli_anything.vision'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-vision=cli_anything.vision:cli']},
)
