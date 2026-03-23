from setuptools import setup
setup(
    name='cli-anything-train',
    version='1.0.0',
    packages=['cli_anything.train'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-train=cli_anything.train:cli']},
)
