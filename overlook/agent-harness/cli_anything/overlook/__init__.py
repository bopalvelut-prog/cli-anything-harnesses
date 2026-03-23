import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('overlook running')
@cli.command()
def start(): click.echo('overlook started')
if __name__ == '__main__': cli()
