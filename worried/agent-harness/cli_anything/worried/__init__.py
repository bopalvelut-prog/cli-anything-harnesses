import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('worried running')
@cli.command()
def start(): click.echo('worried started')
if __name__ == '__main__': cli()
