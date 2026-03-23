import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bin running')
@cli.command()
def start(): click.echo('bin started')
if __name__ == '__main__': cli()
