import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('forget running')
@cli.command()
def start(): click.echo('forget started')
if __name__ == '__main__': cli()
