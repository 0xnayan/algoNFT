from pathlib import Path
from typing import Literal
from beaker import *
from pyteal import *


class NFTs(abi.NamedTuple):
    url: abi.Field[abi.String]
    metadata_hash: abi.Field[abi.StaticArray[abi.Byte, Literal[32]]]
    name: abi.Field[abi.String]
    unitName: abi.Field[abi.String]
    reserve: abi.Field[abi.Address]

    asa = LocalStateValue(stack_type=TealType.uint64, default=Int(0))
    burn_address = LocalStateValue(stack_type= TealType.bytes, default=Bytes("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAY5HFKQ"))
    burntId = LocalStateValue(stack_type= TealType.uint64, default=Int(0))


app = Application("MintNFTs", state=NFTs)

@app.create(bare=True)
def create() -> Expr:
    return app.initialize_global_state()


@app.external(authorize= Authorize.only(Global.creator_address()))
def mintNFTs(requestMint: NFTs, *, output: abi.Uint64) -> Expr:
    name = abi.String()
    unitName = abi.String()
    reserve = abi.Address()
    url = abi.String()
    metadata_hash = abi.make(abi.StaticArray[abi.Byte, Literal[32]])

    return Seq(
        requestMint.name.store_into(name),
        requestMint.unitName.store_into(unitName),
        requestMint.reserve.store_into(reserve),
        requestMint.url.store_into(url),
        requestMint.metadata_hash.store_into(metadata_hash),
        InnerTxnBuilder.Execute(
            {
                TxnField.type_enum: TxnType.AssetConfig,
                TxnField.config_asset_name: name.get(),
                TxnField.config_asset_unit_name: unitName.get(),
                TxnField.config_asset_reserve: reserve.get(),
                TxnField.config_asset_url: url.get(),
                TxnField.config_asset_metadata_hash: metadata_hash.encode(),
                TxnField.config_asset_total: Int(1),
                TxnField.fee: Int(0),
            }
        ),
        output.set(InnerTxn.created_asset_id()),
        app.state.asa.set(InnerTxn.created_asset_id())
    )


@app.external(authorize= Authorize.only(Global.creator_address()))
def transferNFTs(assetId: abi.Uint64, receiver: abi.Address) -> Expr:
    assetId= app.state.asa.get()
    receiver= abi.Address()
    return Seq(

        Assert(app.state.asa == assetId),
        Assert(app.state.burntId != assetId),

        InnerTxnBuilder.Execute(
            {
                TxnField.type_enum: TxnType.AssetTransfer,
                TxnField.asset_receiver: receiver.get(),
                TxnField.xfer_asset: assetId,
                TxnField.asset_amount: Int(1),
            }
    )
)

@app.external(authorize= Authorize.only(Global.creator_address()))
def burn(Id: abi.Uint64) -> Expr:
    burntAddress= app.state.burn_address.get()
    Id= abi.Uint64()
    return Seq(
        Assert(app.state.asa == Id.get()),
        InnerTxnBuilder.Execute(
            {
                TxnField.type_enum: TxnType.AssetTransfer,
                TxnField.asset_receiver: burntAddress,
                TxnField.xfer_asset: Id.get(),
                TxnField.asset_amount: Int(1),
            }
        ),
        app.state.burntId.set(Id.get())
)


if __name__ == "__main__":
    app.build().export(
        Path(__file__).resolve().parent / f"./artifacts/{app.name}"
    )
