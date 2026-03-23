from setuptools import setup
setup(
    name='cli-anything-lock',
    version='1.0.0',
    packages=['cli_anything.lock'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-lock=cli_anything.lock:cli']},
)
