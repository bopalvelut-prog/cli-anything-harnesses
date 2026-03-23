import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('empty running')
@cli.command()
def start(): click.echo('empty started')
if __name__ == '__main__': cli()
