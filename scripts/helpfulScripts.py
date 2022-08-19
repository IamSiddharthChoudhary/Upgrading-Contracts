from brownie import network, accounts, config
import eth_utils

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-cli", "ganache"]


def getAccount(index=None):
    if index:
        return accounts[index]
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts.add(config["networks"][network.show_active()]["privateKey"])
    else:
        return accounts[0]


def encodeFunctionData(indentifier=None, *args):
    if len(args) == 0 or not indentifier:
        return eth_utils.to_bytes(hexstr="0x")
    return indentifier.encode_input(*args)


def upgradeContract(
    proxyContract, newImplementation, proxy_admin_contract=None, encodedData=None, *args
):
    if proxy_admin_contract:
        if encodedData:
            return proxy_admin_contract.upgradeAndCall(
                proxyContract.address,
                newImplementation.address,
                encodedData,
                {"from": getAccount()},
            )
        else:
            return proxy_admin_contract.upgrade(
                proxyContract.address, newImplementation.address, {"from": getAccount()}
            )
    else:
        if encodedData:
            return proxyContract.upgradeToAndCall(
                newImplementation.address, encodedData, {"from": getAccount()}
            )
        else:
            return proxyContract.upgradeTo(
                newImplementation.address, {"from": getAccount()}
            )
