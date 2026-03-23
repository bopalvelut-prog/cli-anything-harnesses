from setuptools import setup
setup(
    name='cli-anything-scene',
    version='1.0.0',
    packages=['cli_anything.scene'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-scene=cli_anything.scene:cli']},
)
