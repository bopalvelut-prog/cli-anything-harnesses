import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bound running')
@cli.command()
def start(): click.echo('bound started')
if __name__ == '__main__': cli()
