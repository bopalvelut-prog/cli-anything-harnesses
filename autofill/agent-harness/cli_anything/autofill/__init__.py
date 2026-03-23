import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('autofill running')
@cli.command()
def start(): click.echo('autofill started')
if __name__ == '__main__': cli()
