import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('fiber running')
@cli.command()
def start(): click.echo('fiber started')
if __name__ == '__main__': cli()
