from setuptools import setup
setup(
    name='cli-anything-clojure',
    version='1.0.0',
    packages=['cli_anything.clojure'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-clojure=cli_anything.clojure:cli']},
)
