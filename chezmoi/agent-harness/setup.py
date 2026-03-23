from setuptools import setup
setup(
    name='cli-anything-chezmoi',
    version='1.0.0',
    packages=['cli_anything.chezmoi'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-chezmoi=cli_anything.chezmoi:cli']},
)
