import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('revolutionary running')
@cli.command()
def start(): click.echo('revolutionary started')
if __name__ == '__main__': cli()
