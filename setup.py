from setuptools import find_packages, setup
import onnxslim


setup(
    name="onnxslim",
    version=onnxslim.__version__,
    description="OnnxSlim: A Toolkit to Help Optimizer Onnx Model",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/inisis/OnnxSlim",
    author="inisis",
    author_email="desmond.yao@buaa.edu.cn",
    project_urls={
        "Bug Tracker": "https://github.com/inisis/OnnxSlim/issues",
    },        
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        'Intended Audience :: Developers',
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    license="MIT",
    install_requires=["loguru", "tabulate", "onnx"],
    packages=find_packages(exclude=("tests", "tests.*")),
    entry_points={"console_scripts": ["onnxslim=onnxslim.cli:main"]},
    zip_safe=True,
    python_requires=">=3.6",
)
