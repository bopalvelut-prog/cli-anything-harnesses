import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('miracle running')
@cli.command()
def start(): click.echo('miracle started')
if __name__ == '__main__': cli()
