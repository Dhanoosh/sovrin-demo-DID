# sovrin-demo-DID
Demo illustrating DID creation using Sovrin on Hyperledger Indy for decentralized identity verification

## Installation

### Installing `indy` package

To utilize the Sovrin functionalities in Python, you need the `indy` package. Install it using `pip`:

```bash
pip install python3-indy
```

### Genesis Transaction File

The genesis transaction file contains the initial transactions for setting up a Sovrin or Hyperledger Indy network. It's essential for nodes to bootstrap and connect to the network.

- **Local Development**: For a local test network, tools like `indy-node` and `indy-plenum` provide scripts to generate a genesis transaction file.
  
- **Sovrin Networks**: For Sovrin's main and test networks, use the predefined genesis files. For a private network, the genesis transaction file is provided during setup.

Replace the placeholder path in the code (`"/path/to/your/private_genesis.txn"`) with the actual path to your genesis transaction file.

## Usage

After setting up, run the provided Python script to demonstrate the creation of a DID using Sovrin within the PEMT-CoSim environment.

## Source
This code is adapted from the [Hyperledger Indy SDK documentation](https://github.com/hyperledger/indy-sdk)
