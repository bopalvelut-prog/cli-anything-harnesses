from setuptools import setup
setup(
    name='cli-anything-survive',
    version='1.0.0',
    packages=['cli_anything.survive'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-survive=cli_anything.survive:cli']},
)
