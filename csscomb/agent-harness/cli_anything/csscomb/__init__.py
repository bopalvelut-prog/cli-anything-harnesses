import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('csscomb running')
@cli.command()
def start(): click.echo('csscomb started')
if __name__ == '__main__': cli()
