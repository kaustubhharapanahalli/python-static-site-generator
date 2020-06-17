import typer
from ssg.site import Site


def main(source="content", dest="dist"):
    config = {
        "source": source,
        "dest": dest
    }

    site = Site(config.get("source"), config.get("dest"))
    site.build()

typer.run(main())
