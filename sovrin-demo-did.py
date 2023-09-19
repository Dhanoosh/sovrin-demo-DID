from indy import did
import asyncio

async def create_did_demo():
    # Create a new pool configuration for your private network
    pool_name = "private_pool"
    pool_config = {"genesis_txn": "/path/to/your/private_genesis.txn"}

    # Set the wallet configuration
    wallet_config = {"id": "wallet1"}
    wallet_credentials = {"key": "wallet_key"}

    # Create and open a new wallet
    await wallet.create_wallet(wallet_config, wallet_credentials)
    wallet_handle = await wallet.open_wallet(wallet_config, wallet_credentials)

    # Create a new DID
    (my_did, my_verkey) = await did.create_and_store_my_did(wallet_handle, "{}")

    print("DID:", my_did)
    print("Verkey:", my_verkey)

    # Close the wallet
    await wallet.close_wallet(wallet_handle)

# Run the demo
asyncio.get_event_loop().run_until_complete(create_did_demo())
