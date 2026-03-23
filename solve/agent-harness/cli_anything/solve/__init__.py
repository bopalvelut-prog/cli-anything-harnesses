import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('solve running')
@cli.command()
def start(): click.echo('solve started')
if __name__ == '__main__': cli()
