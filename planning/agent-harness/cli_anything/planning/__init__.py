import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('planning running')
@cli.command()
def start(): click.echo('planning started')
if __name__ == '__main__': cli()
