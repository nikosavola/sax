
import sax

__all__ = ["flatten_netlist", "netlist"]

def netlist(
    netlist: sax.AnyNetlist, *, top_level_name: str = "top_level",
) -> sax.RecursiveNetlist: ...
def flatten_netlist(recnet: sax.RecursiveNetlist, sep: str = "~") -> sax.Netlist: ...
