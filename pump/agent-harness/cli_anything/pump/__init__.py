import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pump running')
@cli.command()
def start(): click.echo('pump started')
if __name__ == '__main__': cli()
