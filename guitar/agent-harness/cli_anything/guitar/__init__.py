import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('guitar running')
@cli.command()
def start(): click.echo('guitar started')
if __name__ == '__main__': cli()
