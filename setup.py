import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pysolscan",
    version="0.0.5",
    author="Aryabh",
    author_email="aryabharise@gmail.com",
    description="Minimal python wrapper for Solscan.io Api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aryabhthakur/pysolscan",
    project_urls={
        "Bug Tracker": "https://github.com/aryabhthakur/pysolscan/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)