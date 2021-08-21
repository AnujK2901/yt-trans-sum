import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="yt_trans_sum",
    version="1.0.0",
    author="Anuj Kumar",
    author_email="anujkumar29012000@gmail.com",
    description="A small light-weight package to summarize transcript of an eligible YouTube Video. The video should "
                "have well formatted closed-captions to perform summarization by various techniques.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AnujK2901/yt-trans-sum",
    project_urls={
        "Bug Tracker": "https://github.com/AnujK2901/yt-trans-sum/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=[
        'requests',
    ],
)
