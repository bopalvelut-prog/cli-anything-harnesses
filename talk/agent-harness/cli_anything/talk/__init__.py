import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('talk running')
@cli.command()
def start(): click.echo('talk started')
if __name__ == '__main__': cli()
