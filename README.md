# algoNFT

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#features">Features</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

  <p align="center">
   This project aims to design and develop a secure and fully-functional Non-Fungible Token (NFT) contract using Pyteal, adhering to the ERC-721 standard. The contract allows users to create, transfer, and burn NFTs while ensuring the integrity of ownership and preventing fraudulent activities.
Deployed to testnet at : https://app.dappflow.org/explorer/transaction/S5WMTENJDTSDYQV36L2JRJ5FCAPNVAGNMLMEP5SAPHCLVQ2CXZXQ
  </p>
</div>

### Features
- Unique Identifier: Each NFT is assigned a unique identifier for easy tracking and authentication.
- Name and Description: NFTs have associated names and descriptions to provide meaningful context.
- URI Support: Utilizes Uniform Resource Identifiers (URIs) to conveniently access metadata associated with each NFT.
- Pricing: NFTs are priced, providing a clear value for each token.
- Minting: Users can create new NFTs through the contract.
- Transfer: NFTs can be seamlessly transferred from one user to another.
- Burning: Allows users to destroy NFTs when needed.

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

Before you can start using the NFT minting project, you need to have the following tools installed in your computer:
- AlgoKit
- python3.10
- pipx
- git
- docker

### Installation

Required steps for installing the project:

1. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
2. Open a terminal and navigate to the project directory.
3. Run the contract
   ```sh
   python3 mint_nfts.py
   ```
   it will generate the teal and the json files.

<!-- USAGE EXAMPLES -->
## Usage

### For deployment on testnet:
1. open app.dappflow.org, connect a wallet and change the network to testnet:
2. go to abi studio then upload the json and teal files then create app 
3. Now you are ready to go for mint in the test network by providing some details like below
 ```sh
   nftURI,metadata,NFTname,unitName,ReserveAddress(whereToStore)
   ```
4. after that will will be able to transfer and burn the nft

<!-- CONTRIBUTING -->
## Contributing

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- CONTACT -->
## Contact

- borahnayanmoni80@gmail.com
