import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cloudflare_tunnel running')
@cli.command()
def start(): click.echo('cloudflare_tunnel started')
if __name__ == '__main__': cli()
