import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sign running')
@cli.command()
def start(): click.echo('sign started')
if __name__ == '__main__': cli()
