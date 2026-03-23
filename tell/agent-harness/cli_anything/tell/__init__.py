import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tell running')
@cli.command()
def start(): click.echo('tell started')
if __name__ == '__main__': cli()
