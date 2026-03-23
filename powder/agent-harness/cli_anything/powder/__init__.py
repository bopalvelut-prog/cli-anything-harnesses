import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('powder running')
@cli.command()
def start(): click.echo('powder started')
if __name__ == '__main__': cli()
