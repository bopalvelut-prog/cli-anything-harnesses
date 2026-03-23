import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('recruit running')
@cli.command()
def start(): click.echo('recruit started')
if __name__ == '__main__': cli()
