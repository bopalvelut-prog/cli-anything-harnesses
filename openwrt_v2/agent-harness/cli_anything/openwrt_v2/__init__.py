import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('openwrt_v2 running')
@cli.command()
def start(): click.echo('openwrt_v2 started')
if __name__ == '__main__': cli()
