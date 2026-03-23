import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('jewel running')
@cli.command()
def start(): click.echo('jewel started')
if __name__ == '__main__': cli()
