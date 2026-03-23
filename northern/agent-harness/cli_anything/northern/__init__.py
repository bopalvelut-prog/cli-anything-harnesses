import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('northern running')
@cli.command()
def start(): click.echo('northern started')
if __name__ == '__main__': cli()
