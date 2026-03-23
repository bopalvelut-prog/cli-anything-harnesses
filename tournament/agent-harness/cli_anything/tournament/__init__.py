import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tournament running')
@cli.command()
def start(): click.echo('tournament started')
if __name__ == '__main__': cli()
