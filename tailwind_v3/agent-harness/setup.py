from setuptools import setup
setup(
    name='cli-anything-tailwind_v3',
    version='1.0.0',
    packages=['cli_anything.tailwind_v3'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-tailwind_v3=cli_anything.tailwind_v3:cli']},
)
