import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('libffi running')
@cli.command()
def start(): click.echo('libffi started')
if __name__ == '__main__': cli()
