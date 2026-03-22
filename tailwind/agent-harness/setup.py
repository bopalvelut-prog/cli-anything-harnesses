from setuptools import setup
setup(
    name='cli-anything-tailwind',
    version='1.0.0',
    packages=['cli_anything.tailwind'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tailwind=cli_anything.tailwind:cli']},
)
