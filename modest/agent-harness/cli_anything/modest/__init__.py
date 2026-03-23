import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('modest running')
@cli.command()
def start(): click.echo('modest started')
if __name__ == '__main__': cli()
