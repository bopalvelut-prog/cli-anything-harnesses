import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('amazon_lightsail running')
@cli.command()
def start(): click.echo('amazon_lightsail started')
if __name__ == '__main__': cli()
