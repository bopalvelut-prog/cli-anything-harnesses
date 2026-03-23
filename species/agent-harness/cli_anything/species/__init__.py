import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('species running')
@cli.command()
def start(): click.echo('species started')
if __name__ == '__main__': cli()
