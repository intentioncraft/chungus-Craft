# GRANDKILLER90'S HEVY WEAPON
import roblox
import asyncio
from roblox import Client, AssetNotFound
import time
token = "287DE8B8FCD2E9AED0AA888BBDC25AB846E38C0646229CC9697CC17E7E78B4832EAB433C9FF55C214DE32F92CC6270217C1DFD42C96043D47A5549274F323EF6E00492329857D88E94B4DCC2C553A767B5E4E079C4183BB14EB2052284A5C10FB32CB48031C526AEFE54497F9C6BF7665A1D2FCB0A284B1A6720C7EA89B1E29EFC546F750A2FE8BA6AB0DEA27DF64C2504BADB56244EE7E4BB67D1F1A33A90465D7830858AF77D819A8B5CCBA97B99B82A9B55E1DF633FC2F844430BF6397329BEA29B51F5E59DE0A0823352CC25FB7D4F65CC78C29112EC3D7421C3BA5E010E86A1D9F1754832D7DCC11140707F8120526B291558EA5B1722F9EA835433E6FBA4A7395AE8B16A5B22CBE052584E4A03ED698EBCF19A9BA71460DF62DC0AF36D672811F411E00B54DF77F73B6A59384C09FBD8475F8A3E0C836B84791300C70A8FA31AD87E77D3FC0CE55022BBD122328CD24E84EF20C50B114305FF7E1143AF368D9EC2A8B6A79B0F48BB94077722D1E2F76E5759C8E37CEB8B699D5E60B0414A79E562"
client = Client(token)


async def real_asset(asset: int)->int:
    try:
        asset = await client.get_asset(asset)
        return asset.creator.id
    except AssetNotFound:
        return False


async def source_was_target(creator, asset: int)->int:
    if 4965800 == creator:
        return asset
    elif 38152945 == creator:
        return asset
    elif 16163154 == creator:
        return asset
    elif 5281530 == creator:
        return asset
    elif 15446362 == creator:
        return asset
    elif 2349949446 == creator:
        return asset
    elif 2005224608 == creator:
        return asset
    elif 106575032 == creator:
        return asset
    elif 81516065 == creator:
        return asset
    elif 1209085664 == creator:
        return asset
    elif 59805053 == creator:
        return asset
    elif 593881997 == creator:
        return asset
    elif 356976584 == creator:
        return asset
    elif 40633391 == creator:
        return asset
    elif 5815889 == creator:
        return asset
    else:
        return False


async def connector(asset:int) -> int:
    existstate = await real_asset(asset)
    if existstate:
        relevancestate = await source_was_target(existstate, asset)
        if relevancestate:
            return asset
    return False


async def main():
    for i in range(9000000000, 9998778209):
        buffer = await connector(i)
        if buffer:
            print(buffer)
        time.sleep(1)

asyncio.get_event_loop().run_until_complete(main())
