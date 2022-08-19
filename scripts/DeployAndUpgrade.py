from scripts.helpfulScripts import getAccount, encodeFunctionData, upgradeContract
from brownie import Box, ProxyAdmin, TransparentUpgradeableProxy, Contract, BoxV2


def main():
    account = getAccount()
    contract01 = Box.deploy({"from": account})

    proxy_admin = ProxyAdmin.deploy({"from": account})

    # identifier = contract01.store , 1
    box_encoded_identifier_function = encodeFunctionData()

    proxy = TransparentUpgradeableProxy.deploy(
        contract01.address,
        proxy_admin.address,
        box_encoded_identifier_function,
        {"from": account},
    )

    print(f"Proxy deployed to {proxy}, So you can upgrade your contract")
    proxy_box = Contract.from_abi("Box", proxy.address, Box.abi)
    proxy_box.store(3, {"from": account})

    newContract = BoxV2.deploy({"from": account})
    upgradedContractTxn = upgradeContract(
        proxy, newContract, proxy_admin_contract=proxy_admin
    )
    upgradedContractTxn.wait(1)

    proxy_box = Contract.from_abi("BoxV2", proxy.address, BoxV2.abi)

    print(f"Value in starting is {proxy_box.getValue()}")
    proxy_box.increment({"from": account})
    print(f"Value after incrementing is {proxy_box.getValue()}")
