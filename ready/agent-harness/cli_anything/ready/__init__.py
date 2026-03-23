import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ready running')
@cli.command()
def start(): click.echo('ready started')
if __name__ == '__main__': cli()
