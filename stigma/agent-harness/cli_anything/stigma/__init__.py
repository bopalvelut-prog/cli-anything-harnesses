import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('stigma running')
@cli.command()
def start(): click.echo('stigma started')
if __name__ == '__main__': cli()
