import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('kbfs running')
@cli.command()
def start(): click.echo('kbfs started')
if __name__ == '__main__': cli()
