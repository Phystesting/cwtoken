import setuptools

setuptools.setup(
    name="cw_api",
    version="0.1.0",
    author="Connor Crawford",
    description="Package handling tokens and URLs",
    packages=setuptools.find_packages(),
    install_requires=[
        "pandas",
        "requests"
    ],
    python_requires='>=3.7',
)