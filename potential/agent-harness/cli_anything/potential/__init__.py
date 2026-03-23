import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('potential running')
@cli.command()
def start(): click.echo('potential started')
if __name__ == '__main__': cli()
