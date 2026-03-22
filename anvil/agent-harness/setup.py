from setuptools import setup
setup(
    name='cli-anything-anvil',
    version='1.0.0',
    packages=['cli_anything.anvil'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-anvil=cli_anything.anvil:cli']},
)
