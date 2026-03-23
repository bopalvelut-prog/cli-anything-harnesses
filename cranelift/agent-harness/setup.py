from setuptools import setup
setup(
    name='cli-anything-cranelift',
    version='1.0.0',
    packages=['cli_anything.cranelift'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-cranelift=cli_anything.cranelift:cli']},
)
