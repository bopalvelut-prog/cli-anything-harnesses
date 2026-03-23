import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('story running')
@cli.command()
def start(): click.echo('story started')
if __name__ == '__main__': cli()
