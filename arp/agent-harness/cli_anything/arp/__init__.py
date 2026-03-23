import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('arp running')
@cli.command()
def start(): click.echo('arp started')
if __name__ == '__main__': cli()
