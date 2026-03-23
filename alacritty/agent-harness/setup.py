from setuptools import setup
setup(
    name='cli-anything-alacritty',
    version='1.0.0',
    packages=['cli_anything.alacritty'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-alacritty=cli_anything.alacritty:cli']},
)
