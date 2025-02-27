
async def window1_get_data(**kwargs):
    return {
        "something": "data from Window1 getter",
    }


async def window2_get_data(**kwargs):
    return {
        "something": "data from Window2 getter",
    }


async def dialog_get_data(**kwargs):
    return {
        "name": "хуесос",
    }