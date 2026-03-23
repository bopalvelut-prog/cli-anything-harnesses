import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('marriage running')
@cli.command()
def start(): click.echo('marriage started')
if __name__ == '__main__': cli()
