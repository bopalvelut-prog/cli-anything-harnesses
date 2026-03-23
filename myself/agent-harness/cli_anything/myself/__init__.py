import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('myself running')
@cli.command()
def start(): click.echo('myself started')
if __name__ == '__main__': cli()
