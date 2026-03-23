from setuptools import setup
setup(
    name='cli-anything-onnx',
    version='1.0.0',
    packages=['cli_anything.onnx'],
    install_requires=['click'],
    entry_points={'console_scripts': ['cli-anything-onnx=cli_anything.onnx:cli']},
)
