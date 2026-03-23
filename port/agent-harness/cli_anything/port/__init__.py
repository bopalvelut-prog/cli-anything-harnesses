import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('port running')
@cli.command()
def start(): click.echo('port started')
if __name__ == '__main__': cli()
