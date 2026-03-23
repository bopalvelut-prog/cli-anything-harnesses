import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dendrite running')
@cli.command()
def start(): click.echo('dendrite started')
if __name__ == '__main__': cli()
