import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cloudflare_warp running')
@cli.command()
def start(): click.echo('cloudflare_warp started')
if __name__ == '__main__': cli()
