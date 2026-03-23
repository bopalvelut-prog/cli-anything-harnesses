import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('vocabulary running')
@cli.command()
def start(): click.echo('vocabulary started')
if __name__ == '__main__': cli()
