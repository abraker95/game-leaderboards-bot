from cmd_core import Cmd



@Cmd.metadata(
    perm = [
        Cmd.perm.PUBLIC
    ],
    info = '',
    args = {
    }
)
async def score(msg, logger, **kargs):
    pass
    return Cmd.ok()