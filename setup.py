from setuptools import setup, find_packages

setup(
    name="jagare",
    description="The RPC of Jagare",
    author="CodeDouban Team",
    url="http://code.dapps.douban.com/xutao/jagare-rpc",
    packages=find_packages(exclude=["tests", "jagare_client", "service_gen"])
)
