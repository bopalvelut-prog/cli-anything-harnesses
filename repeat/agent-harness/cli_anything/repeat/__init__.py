import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('repeat running')
@cli.command()
def start(): click.echo('repeat started')
if __name__ == '__main__': cli()
