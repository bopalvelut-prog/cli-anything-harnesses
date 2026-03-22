from setuptools import setup
setup(
    name='cli-anything-craft_cms',
    version='1.0.0',
    packages=['cli_anything.craft_cms'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-craft_cms=cli_anything.craft_cms:cli']},
)
