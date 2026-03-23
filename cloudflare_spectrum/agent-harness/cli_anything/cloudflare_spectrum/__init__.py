import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cloudflare_spectrum running')
@cli.command()
def start(): click.echo('cloudflare_spectrum started')
if __name__ == '__main__': cli()
