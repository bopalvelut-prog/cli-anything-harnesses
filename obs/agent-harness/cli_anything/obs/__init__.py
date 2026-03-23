import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('obs running')
@cli.command()
def start(): click.echo('obs started')
if __name__ == '__main__': cli()
