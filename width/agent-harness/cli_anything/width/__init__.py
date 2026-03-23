import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('width running')
@cli.command()
def start(): click.echo('width started')
if __name__ == '__main__': cli()
