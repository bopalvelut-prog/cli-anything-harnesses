import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('guilt running')
@cli.command()
def start(): click.echo('guilt started')
if __name__ == '__main__': cli()
