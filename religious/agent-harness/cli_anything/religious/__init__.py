import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('religious running')
@cli.command()
def start(): click.echo('religious started')
if __name__ == '__main__': cli()
