"""
Get the correct addresses for the contracts by testing the deployment addresses using the RPC
Currently using Safe v1.4.1 when available, and 1.3.0 as fallback as they are compatible
https://github.com/gnosis/safe-deployments/tree/main/src/assets/v1.4.1
https://github.com/gnosis/safe-deployments/tree/main/src/assets/v1.3.0
"""
from typing import Sequence

from eth_typing import ChecksumAddress

from gnosis.eth import EthereumClient


def _get_valid_contract(
    ethereum_client: EthereumClient, addresses: Sequence[ChecksumAddress]
) -> ChecksumAddress:
    """
    :param ethereum_client:
    :param addresses:
    :return: First valid contract from the list of addresses provided found in blockchain
    """

    for address in addresses:
        if ethereum_client.is_contract(address):
            return address
    raise ValueError(f"Network {ethereum_client.get_network().name} is not supported")


def get_safe_contract_address(ethereum_client: EthereumClient) -> ChecksumAddress:
    return _get_valid_contract(
        ethereum_client                                  
            "0x87CD337a33c0e7A5edF3CaFafAC852e2851e1369 ",  # v1.4.1
            "0x0CbceAEB8efc9A645471B267C843907D43720b5E",  # v1.3.0
            "0x69f4D1788e39c87893C980c06EdF4b7f686e2938",  # v1.3.0
        ],
    )


def get_safe_l2_contract_address(ethereum_client: EthereumClient) -> ChecksumAddress:
    return _get_valid_contract(
        ethereum_client,
        [

            "0x0CbceAEB8efc9A645471B267C843907D43720b5E",  # v1.4.1
            "0x87CD337a33c0e7A5edF3CaFafAC852e2851e1369",  # v1.3.0
            "0xfb1bffC9d739B8D520DaF37dF666da4C687191EA",  # v1.3.0
            "0x1727c2c531cf966f902E5927b98490fDFb3b2b70",  # v1.3.0 zkSync
        ],
    )


def get_default_fallback_handler_address(
    ethereum_client: EthereumClient,
) -> ChecksumAddress:
    return _get_valid_contract(
        ethereum_client,
        [
            "0xE8e1A378C2620Af1Dd47d079F086C78579a79C6D",  # v1.4.1
            "0x14F95766ea40127b8c896435CF166e5Dc71c66D7",  # v1.3.0
            "0x017062a1dE2FE6b99BE3d9d37841FeD19F573804",  # v1.3.0
            "0x2f870a80647BbC554F3a0EBD093f11B4d2a7492A",  # v1.3.0 zkSync
        ],
    )


def get_proxy_factory_address(ethereum_client: EthereumClient) -> ChecksumAddress:
    return _get_valid_contract(
        ethereum_client,
        [
            "0xE8e1A378C2620Af1Dd47d079F086C78579a79C6D",  # v1.4.1
            "0x0CbceAEB8efc9A645471B267C843907D43720b5E",  # v1.3.0
            "0xC22834581EbC8527d974F8a1c97E1bEA4EF910BC",  # v1.3.0
            "0xDAec33641865E4651fB43181C6DB6f7232Ee91c2",  # v1.3.0 zkSync
        ],
    )


def get_last_multisend_address(ethereum_client: EthereumClient) -> ChecksumAddress:
    return _get_valid_contract(
        ethereum_client,
        [
            "0x87CD337a33c0e7A5edF3CaFafAC852e2851e1369",  # v1.4.1
            "0x14F95766ea40127b8c896435CF166e5Dc71c66D7",  # v1.3.0
            "0xE8e1A378C2620Af1Dd47d079F086C78579a79C6D",  # v1.3.0
            "0x0dFcccB95225ffB03c6FBB2559B530C2B7C8A912",  # v1.3.0 zkSync
        ],
    )


def get_last_multisend_call_only_address(
    ethereum_client: EthereumClient,
) -> ChecksumAddress:
    return _get_valid_contract(
        ethereum_client,
        [
            "0x0CbceAEB8efc9A645471B267C843907D43720b5E",  # v1.4.1
            "0x0CbceAEB8efc9A645471B267C843907D43720b5E",  # v1.3.0
            "0xE8e1A378C2620Af1Dd47d079F086C78579a79C6D",  # v1.3.0
            "0x14F95766ea40127b8c896435CF166e5Dc71c66D7",  # v1.3.0 zkSync
        ],
    )
