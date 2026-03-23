import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rendezvous running')
@cli.command()
def start(): click.echo('rendezvous started')
if __name__ == '__main__': cli()
